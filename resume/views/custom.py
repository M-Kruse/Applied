import os

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from resume.models import (Employment, Applicant, Experience,
                     Education, Resume, Domain, Reference,
                     Project, Duty, Template)

def preview_template(request):
    resumes = Resume.objects.get().order_by("id")
    my_resume = resumes.filter(id=kwargs.get('pk'))
    my_template = my_resume.template
    with open(my_template.file, 'r') as fp:
        data = fp.read()
    served_filename = 'test.docx'
    response = HttpResponse(mimetype="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    response.write(data)
    return response


def view_template(request, *args, **kwargs):
    template = Template.objects.get(pk=kwargs.get('pk'))
    filename = template.file.path
    data = open(filename, "rb").read()
    response = HttpResponse(data, content_type='application/vnd')
    response['Content-Length'] = os.path.getsize(filename)
    response['Content-Disposition'] = 'attachment; filename="{0}"'.format(filename.split('/')[-1])

    return response

def build_resume_from_docx_template(request, *args, **kwargs):
    my_resume = Resume.objects.get(pk=kwargs.get('pk'))
    preview_format = my_resume.output_format
    template_path = my_resume.template.file
    resume_json = create_resume_json(kwargs.get('pk'))
    from docxtpl import DocxTemplate
    #template_path = "/media/uploads/example_resume_template.docx"
    doc = DocxTemplate(template_path)
    doc.render(resume_json)
    if kwargs.get('filename'):
        filename = kwargs.get('filename')
    else:
        filename = "preview_resume.docx"
    new_doc = "/media/{0}".format(filename)
    doc.save(new_doc)
    data = open(new_doc, "rb").read()
    response = HttpResponse(data, content_type='application/vnd')
    response['Content-Length'] = os.path.getsize(new_doc)
    response['Content-Disposition'] = 'attachment; filename="{0}"'.format(filename)
    return response


def create_resume_json(pk):
    resume = Resume.objects.get(pk=pk)
    applicant = Applicant.objects.get(pk=resume.applicant.id)
    resume_json = {
        "contact_info": {
            "name": applicant.name,
            "email": applicant.email,
            "phone": applicant.phone,
            },
        "employments":[],
        "experiences":[],
        "education":[],
        "references":[]
        }
    employments = applicant.employment.all()
    for e in employments:
        employment_json = {
            "company_name": e.company_name,
            "job_title": e.job_title,
            "start_date": e.start_date,
            "end_date": e.end_date,
            "duties": [],
            "projects": [],
        }
        for d in e.duties.all():
            employment_json['duties'].append(d.description)

        for p in e.projects.all():
            employment_json['projects'].append(p.description)
        resume_json['employments'].append(employment_json)
    experiences = applicant.experiences.all()
    d_list = []
    for x in experiences:
        d_list.append(x.domain.name)
    d_list = set(d_list)
    for domain in d_list:
        x_list = []
        for x in experiences:
            if x.domain.name == domain:
                x_list.append(x.name)
        domains_json = {
            domain: x_list
            }
        resume_json['experiences'].append(domains_json)
    education = applicant.education.all()
    for e in education:
        education_json = {
            "school": e.name,
            "level": e.level,
            "year": e.year
            }
        resume_json['education'].append(education_json)
    refs = applicant.reference.all()
    for r in refs:
        reference_json = {
            "name": r.name,
            "employment": r.employment.company_name,
            "contact": r.contact,
        }
        resume_json['references'].append(reference_json)
    return resume_json


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your new Resume account!'
            message = render_to_string('resume/acc/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return render(request, 'resume/acc/acc_confirm.html', {'form': form})
    else:
        form = SignupForm()

    return render(request, 'resume/acc/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return render(request, 'resume/acc/acc_confirmed.html')
    else:
        return render(request, 'resume/acc/acc_token_invalid.html')
