from django.views.generic import UpdateView

from resume.models import (Employment, Applicant, Experience,
                     Education, Resume, Domain, Reference,
                     Project, Duty, Template)

from resume.forms import (ResumeForm, ApplicantForm, DomainForm,
                    ExperienceForm, EducationForm, ReferenceForm,
                    EmploymentForm, ProjectForm, DutyForm, TemplateForm)

from django.http import HttpResponseRedirect

class DomainUpdateView(UpdateView):
    model = Domain
    form_class = DomainForm
    template_name = 'resume/domain/domain_update_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # Any manual settings go here
        self.object.save()
        return HttpResponseRedirect('/resume/experience/')

    def dispatch(self, request, *args, **kwargs):
        return super(DomainUpdateView, self).dispatch(request, *args, **kwargs)

class ExperienceUpdateView(UpdateView):
    model = Experience
    form_class = ExperienceForm
    template_name = 'resume/xp/xp_update_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # Any manual settings go here
        self.object.save()
        return HttpResponseRedirect('/resume/experience/')

    def dispatch(self, request, *args, **kwargs):
        return super(ExperienceUpdateView, self).dispatch(request, *args, **kwargs)

class EducationUpdateView(UpdateView):
    model = Education
    form_class = EducationForm
    template_name = 'resume/edu/edu_update_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # Any manual settings go here
        self.object.save()
        return HttpResponseRedirect('/resume/education/')

    def dispatch(self, request, *args, **kwargs):
        return super(EducationUpdateView, self).dispatch(request, *args, **kwargs)

class ReferenceUpdateView(UpdateView):
    model = Reference
    form_class = ReferenceForm
    template_name = 'resume/ref/ref_update_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # Any manual settings go here
        self.object.save()
        return HttpResponseRedirect('/resume/reference/')

    def dispatch(self, request, *args, **kwargs):
        return super(ReferenceUpdateView, self).dispatch(request, *args, **kwargs)

class EmploymentUpdateView(UpdateView):
    model = Employment
    form_class = EmploymentForm
    template_name = 'resume/employment/employment_update_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # Any manual settings go here
        self.object.save()
        return HttpResponseRedirect('/resume/employment/')

    def dispatch(self, request, *args, **kwargs):
        return super(EmploymentUpdateView, self).dispatch(request, *args, **kwargs)

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'resume/project/project_update_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # Any manual settings go here
        self.object.save()
        return HttpResponseRedirect('/resume/project/')

    def dispatch(self, request, *args, **kwargs):
        return super(ProjectUpdateView, self).dispatch(request, *args, **kwargs)

class DutyUpdateView(UpdateView):
    model = Duty
    form_class = DutyForm
    template_name = 'resume/duty/duty_update_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # Any manual settings go here
        self.object.save()
        return HttpResponseRedirect('/resume/duty/')

    def dispatch(self, request, *args, **kwargs):
        return super(DutyUpdateView, self).dispatch(request, *args, **kwargs)

class ApplicantUpdateView(UpdateView):
    model = Applicant
    form_class = ApplicantForm
    template_name = 'resume/applicant/app_update_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # Any manual settings go here
        self.object.save()
        return HttpResponseRedirect('/resume/applicant/')
        #return HttpResponseRedirect(self.object.get_absolute_url())

    def dispatch(self, request, *args, **kwargs):
        return super(ApplicantUpdateView, self).dispatch(request, *args, **kwargs)

class ResumeUpdateView(UpdateView):
    model = Resume
    form_class = ResumeForm
    template_name = 'resume/resume_update_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # Any manual settings go here
        self.object.save()
        return HttpResponseRedirect('/resume/')

    def dispatch(self, request, *args, **kwargs):
        return super(ResumeUpdateView, self).dispatch(request, *args, **kwargs)

class TemplateUpdateView(UpdateView):
    model = Template
    form_class = TemplateForm
    template_name = 'resume/template/template_update_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/resume/template/')

    def dispatch(self, request, *args, **kwargs):
        return super(ResumeUpdateView, self).dispatch(request, *args, **kwargs)
