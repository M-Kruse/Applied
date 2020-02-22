from django.urls import reverse
from django.views.generic import DeleteView

from resume.models import (Employment, Applicant, Experience,
                     Education, Resume, Domain, Reference,
                     Project, Duty, Template)

class DomainDeleteView(DeleteView):
    model = Domain

    def get_success_url(self):
        return reverse('resume:domain')

    def dispatch(self, request, *args, **kwargs):
        return super(DomainDeleteView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class ExperienceDeleteView(DeleteView):
    model = Experience

    def get_success_url(self):
        return reverse('resume:xp')

    def dispatch(self, request, *args, **kwargs):
        return super(ExperienceDeleteView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class ResumeDeleteView(DeleteView):
    model = Resume

    def get_success_url(self):
        return reverse('resume:resumes')

    def dispatch(self, request, *args, **kwargs):
        return super(ResumeDeleteView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class ApplicantDeleteView(DeleteView):
    model = Applicant

    def get_success_url(self):
        return reverse('resume:applicants')

    def dispatch(self, request, *args, **kwargs):
        return super(ApplicantDeleteView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class EmploymentDeleteView(DeleteView):
    model = Employment

    def get_success_url(self):
        return reverse('resume:employments')

    def dispatch(self, request, *args, **kwargs):
        return super(EmploymentDeleteView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class ReferenceDeleteView(DeleteView):
    model = Reference

    def get_success_url(self):
        return reverse('resume:refs')

    def dispatch(self, request, *args, **kwargs):
        return super(ReferenceDeleteView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class EducationDeleteView(DeleteView):
    model = Education

    def get_success_url(self):
        return reverse('resume:edus')

    def dispatch(self, request, *args, **kwargs):
        return super(EducationDeleteView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class ProjectDeleteView(DeleteView):
    model = Project

    def get_success_url(self):
        return reverse('resume:projects')

    def dispatch(self, request, *args, **kwargs):
        return super(ProjectDeleteView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class DutyDeleteView(DeleteView):
    model = Duty

    def get_success_url(self):
        return reverse('resume:duties')

    def dispatch(self, request, *args, **kwargs):
        return super(DutyDeleteView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class TemplateDeleteView(DeleteView):
    model = Template

    def get_success_url(self):
        return reverse('resume:templates')

    def dispatch(self, request, *args, **kwargs):
        return super(TemplateDeleteView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
