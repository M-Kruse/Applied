import os

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic import TemplateView, UpdateView, DeleteView

from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User

from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.template.loader import render_to_string

from django.core.mail import EmailMessage

from resume.tokens import account_activation_token

from resume.models import (Employment, Applicant, Experience,
                     Education, Resume, Domain, Reference,
                     Project, Duty, Template)

from resume.forms import (ResumeForm, ApplicantForm, DomainForm,
                    ExperienceForm, EducationForm, ReferenceForm,
                    EmploymentForm, ProjectForm, DutyForm, TemplateForm)

from resume.forms import SignupForm

class IndexView(generic.ListView):
    template_name = 'resume/index.html'

    def get_queryset(self):
        self.request.session['isWizard'] = False
        """Return the Employment objects questions."""
        return None

class HTMLView(generic.ListView):
    model = Employment
    template_name = 'resume/resume.html'
    context_object_name = 'employment_list'

    def get_queryset(self):
        resume = Resume.objects.get(owner=self.request.user)
        return resume.applicant.employment.all

    def get_context_data(self, **kwargs):
        resume = Resume.objects.get(pk=self.kwargs.get('pk'))
        """Call the base implementation first to get a context """
        context = super(HTMLView, self).get_context_data(**kwargs)
        """ Add extra context from another model """
        context['applicant'] = Applicant.objects.get(pk=resume.applicant.id)
        return context

class JSONResponseMixin:

    def render_to_json_response(self, context, **response_kwargs):

        return JsonResponse(
            self.get_data(context),
            **response_kwargs
        )

    def get_data(self, context):
        return context

class JSONView(JSONResponseMixin, TemplateView):

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(
            create_resume_json(self.kwargs.get('pk')), **response_kwargs
        )

class ResumeListView(generic.ListView):
    model = Resume
    template_name = 'resume/resume_list.html'
    context_object_name = 'resume_list'

    def get_queryset(self):
        self.request.session['isWizard'] = False
        resume = Resume.objects.all().order_by("id")
        return resume.filter(owner=self.request.user)

class ApplicantListView(generic.ListView):
    model = Applicant
    template_name = 'resume/applicant/applicant_list.html'
    context_object_name = 'app_list'

    def get_queryset(self):
        apps = Applicant.objects.all().order_by("id")
        return apps.filter(owner=self.request.user)


class DomainListView(generic.ListView):
    model = Domain
    template_name = 'resume/domain/domain_list.html'
    context_object_name = 'domain_list'

    def get_queryset(self):
        self.request.session['isWizard'] = False
        domains = Domain.objects.all().order_by("id")
        return domains.filter(owner=self.request.user)

class ExperienceListView(generic.ListView):
    model = Experience
    template_name = 'resume/xp/xp_list.html'
    context_object_name = 'xp_list'

    def get_queryset(self):
        xps = Experience.objects.all().order_by("id")
        return xps.filter(owner=self.request.user)

class EducationListView(generic.ListView):
    model = Education
    template_name = 'resume/edu/edu_list.html'
    context_object_name = 'edu_list'

    def get_queryset(self):
        self.request.session['isWizard'] = False
        edus = Education.objects.all().order_by("id")
        return edus.filter(owner=self.request.user)

class ReferenceListView(generic.ListView):
    model = Reference
    template_name = 'resume/ref/ref_list.html'
    context_object_name = 'ref_list'

    def get_queryset(self):
        self.request.session['isWizard'] = False
        refs = Reference.objects.all().order_by("id")
        return refs.filter(owner=self.request.user)

class EmploymentListView(generic.ListView):
    model = Employment
    template_name = 'resume/employment/employment_list.html'
    context_object_name = 'employment_list'

    def get_queryset(self):
        self.request.session['isWizard'] = False
        employments = Employment.objects.all().order_by("id")
        return employments.filter(owner=self.request.user)

class ProjectListView(generic.ListView):
    model = Project
    template_name = 'resume/project/project_list.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        self.request.session['isWizard'] = False
        projects = Project.objects.all().order_by("id")
        return projects.filter(owner=self.request.user)

class DutyListView(generic.ListView):
    model = Duty
    template_name = 'resume/duty/duty_list.html'
    context_object_name = 'duty_list'

    def get_queryset(self):
        self.request.session['isWizard'] = False
        duties = Duty.objects.all().order_by("id")
        return duties.filter(owner=self.request.user)

class TemplateListView(generic.ListView):
    model = Template
    template_name = 'resume/template/template_list.html'
    context_object_name = 'template_list'

    def get_queryset(self):
        self.request.session['isWizard'] = False
        templates = Template.objects.all().order_by("id")
        return templates.filter(owner=self.request.user)

class ResumeWizardView(generic.ListView):
    template_name = 'resume/wizard_index.html'

    def get_queryset(self):
        self.request.session['isWizard'] = True
        return Resume.objects.all()

class TemplatePreviewView(generic.DetailView):
    template_name = 'resume/wizard_index.html'

    def get_queryset(self):
        self.request.session['isWizard'] = True
        return Resume.objects.all()