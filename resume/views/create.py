from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.core.files.storage import FileSystemStorage

from resume.models import (Employment, Applicant, Experience,
                     Education, Resume, Domain, Reference,
                     Project, Duty, Template, CoverLetter)

from resume.forms import (ResumeForm, ApplicantForm, DomainForm,
                    ExperienceForm, EducationForm, ReferenceForm,
                    EmploymentForm, ProjectForm, DutyForm, TemplateForm,
                    CoverLetterForm)

def new_experience(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            domain = form.cleaned_data['domain']
            e = Experience(owner=request.user, name=name, domain=domain)
            e.save()
            if 'create_another' in request.POST:
                return HttpResponseRedirect('/resume/experience/new')
            else:
                if request.session['isWizard'] == True:
                    return HttpResponseRedirect('/resume/duty/new')
                else:
                    return HttpResponseRedirect('/resume/experience/')
    else:
        form = ExperienceForm()
    return render(request, 'resume/xp/xp_form.html', {'form': form})

def new_domain(request):
    if request.method == 'POST':
        form = DomainForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            d = Domain(owner=request.user, name=name)
            d.save()
            if 'create_another' in request.POST:
                return HttpResponseRedirect('/resume/domain/new')
            else:
                if request.session['isWizard']:
                    return HttpResponseRedirect('/resume/experience/new')
                else:
                    return HttpResponseRedirect('/resume/domain/')
    else:
        form = DomainForm()
    return render(request, 'resume/domain/domain_form.html', {'form': form})

def new_education(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            level = form.cleaned_data['level']
            year = form.cleaned_data['year']
            e = Education(owner=request.user, name=name, level=level, year=year)
            e.save()
        if 'create_another' in request.POST:
            return HttpResponseRedirect('/resume/education/new')
        else:
            if request.session['isWizard']:
                return HttpResponseRedirect('/resume/employment/new')
            else:
                return HttpResponseRedirect('/resume/education/')
    else:
        form = EducationForm()
    return render(request, 'resume/edu/edu_form.html', {'form': form})

def new_reference(request):
    if request.method == 'POST':
        form = ReferenceForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            employment = form.cleaned_data['employment']
            contact = form.cleaned_data['contact']
            r = Reference(owner=request.user, name=name, employment=employment, contact=contact)
            r.save()
            if 'create_another' in request.POST:
                return HttpResponseRedirect('/resume/reference/new')
            else:
                if request.session['isWizard']:
                    return HttpResponseRedirect('/resume/applicant/new')
                else:
                    return HttpResponseRedirect('/resume/reference/')
    else:
        form = ReferenceForm()

    return render(request, 'resume/ref/ref_form.html', {'form': form})

def new_employment(request):
    if request.method == 'POST':
        form = EmploymentForm(request.POST)
        if form.is_valid():
            company_name = form.cleaned_data['company_name']
            job_title = form.cleaned_data['job_title']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            leave_reason = form.cleaned_data['leave_reason']
            duties = form.cleaned_data['duties']
            projects = form.cleaned_data['projects']
            e = Employment(
                owner=request.user,
                company_name=company_name,
                job_title=job_title,
                start_date=start_date,
                end_date=end_date,
                leave_reason=leave_reason,
            )
            e.save()
            e.duties.set(duties)
            e.projects.set(projects)
            if 'create_another' in request.POST:
                return HttpResponseRedirect('/employment/new')
            else:
                if request.session['isWizard']:
                    return HttpResponseRedirect('/resume/reference/new')
                else:
                    return HttpResponseRedirect('/resume/employment/')

    else:
        form = EmploymentForm()

    return render(request, 'resume/employment/employment_form.html', {'form': form})

def new_duty(request):
    if request.method == 'POST':
        form = DutyForm(request.POST)
        if form.is_valid():
            desc = form.cleaned_data['description']
            d = Duty(owner=request.user, description=desc)
            d.save()
            if 'create_another' in request.POST:
                return HttpResponseRedirect('/resume/duty/new')
            else:
                if request.session['isWizard']:
                    return HttpResponseRedirect('/resume/project/new')
                else:
                    return HttpResponseRedirect('/resume/duty/')
    else:
        form = DutyForm()
    return render(request, 'resume/duty/duty_form.html', {'form': form})

def new_template(request):
    upload_dir = "uploads/"
    if request.method == 'POST':
        form = TemplateForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            for filename, file in request.FILES.items():
                file_ref = request.FILES[filename]
                fs = FileSystemStorage()
                filename = fs.save(upload_dir + file_ref.name, file_ref)
            t = Template(owner=request.user, name=name, file=filename)
            t.save()
            if request.session['isWizard']:
                if '/resume/new' in request.META['HTTP_REFERER']:
                    return HttpResponseRedirect('/resume/cover/new')
                else:
                    return HttpResponseRedirect('/resume/new')
            else:
                return HttpResponseRedirect('/resume/template/')
    else:
        form = TemplateForm()
    if '/resume/template/new' in request.META['HTTP_REFERER']:
        template_type = 'Cover Letter'
    else:
        template_type = 'Resume'
    return render(request, 'resume/template/template_form.html', {'form': form, 'type': template_type})

def new_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            desc = form.cleaned_data['description']
            p = Project(owner=request.user, description=desc)
            p.save()
            if 'create_another' in request.POST:
                return HttpResponseRedirect('/resume/project/new')
            else:
                if request.session['isWizard']:
                    return HttpResponseRedirect('/resume/education/new')
                else:
                    return HttpResponseRedirect('/resume/project/')
    else:
        form = ProjectForm()
    return render(request, 'resume/project/project_form.html', {'form': form})

def new_applicant(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            employments = form.cleaned_data['employment']
            experiences = form.cleaned_data['experiences']
            references = form.cleaned_data['reference']
            education = form.cleaned_data['education']
            a = Applicant(owner=request.user, name=name, email=email, phone=phone)
            a.save()
            a.employment.set(employments)
            a.experiences.set(experiences)
            a.reference.set(references)
            a.education.set(education)
            if request.session['isWizard']:
                return HttpResponseRedirect('/resume/template/new')
            else:
                return HttpResponseRedirect('/resume/applicant/')
    else:
        form = ApplicantForm()

    return render(request, 'resume/applicant/applicant_form.html', {'form': form})

def new_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            applicant = form.cleaned_data['applicant']
            output_format = form.cleaned_data['output_format']
            template = form.cleaned_data['template']
            #style = form.cleaned_data['style']
            r = Resume(
                owner=request.user,
                name=name,
                applicant=applicant,
                output_format=output_format,
                template=template
            )
            r.save()
            if request.session['isWizard']:
                return HttpResponseRedirect('/resume/template/new')
            else:
                return HttpResponseRedirect('/resume/')
    else:
        form = ResumeForm()
    return render(request, 'resume/resume_form.html', {'form': form})

def new_cover_letter(request):
    if request.method == 'POST':
        form = CoverLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            summary = form.cleaned_data['summary']
            applicant = form.cleaned_data['applicant']
            output_format = form.cleaned_data['output_format']
            template = form.cleaned_data['template']
            #style = form.cleaned_data['style']
            r = CoverLetter(
                owner=request.user,
                name=name,
                applicant=applicant,
                output_format=output_format,
                template=template,
                summary=summary
            )
            r.save()
            if request.session['isWizard']:
                request.session['isWizard'] = False
                return HttpResponseRedirect('/resume/')
            else:
                return HttpResponseRedirect('/resume/cover')
    else:
        form = CoverLetterForm()
    return render(request, 'resume/cover/cover_form.html', {'form': form})