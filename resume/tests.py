from django.test import TestCase

from django.contrib.auth.models import User

from resume.models import (Employment, Duty, Project, Domain,
                           Experience, Education, Reference, 
                           Applicant, Style, Resume, Template)

from django.test import Client

test_company_name = "AB Corp"
test_job_title = "Button Smasher"
test_start_date = "2020-01-01"
test_end_date = "2020-01-02"
test_leave_reason = "Another button pushing job."
test_duty = "Push buttons in the right order."
test_project = "Improved button pushing processes."
test_domain = "Systems Administration"
test_experience = "Button Pushing"
test_edu = "Foo High School"
test_edu_level = "Diploma"
test_edu_year = "2019-01-01"
test_applicant = "Rusty Shackleford"
test_email = "rustyshack@example.com"
test_phone = "1234567890"
test_ref = "Johnny Doh"
test_ref_contact = "Available Upon Request"
test_resume_name = "Rustys Rez"
test_output_format = "JSON"
test_template_name = "Default"

class DutyTestCase(TestCase):
    def setUp(self):
        test_owner = User.objects.create_user(username='Unittest_owner', password='muhdummypassword')
        self.duty = Duty.objects.create(owner=test_owner, description=test_duty)

    def test_duty(self):
        self.assertEqual(self.duty.description, test_duty)


class ProjectTestCase(TestCase):
    def setUp(self):
        test_owner = User.objects.create_user(username='Unittest_owner', password='muhdummypassword')
        self.project = Project.objects.create(owner=test_owner, description=test_project)

    def test_project(self):
        self.assertEqual(self.project.description, test_project)

class EmploymentTestCase(TestCase):
    def setUp(self):
        test_owner = User.objects.create_user(username='Unittest_owner', password='muhdummypassword')
        Duty.objects.create(owner=test_owner, description=test_duty)
        Project.objects.create(owner=test_owner, description=test_project)
        self.employment = Employment.objects.create(
            owner=test_owner,
            company_name=test_company_name,
            job_title=test_job_title,
            start_date=test_start_date,
            end_date=test_end_date,
            leave_reason=test_leave_reason
        )
        my_duties = [Duty.objects.get(description=test_duty)]
        self.employment.duties.set(my_duties)
        my_projects = [Project.objects.get(description=test_project)]
        self.employment.projects.set(my_projects)

    def test_employment(self):
        self.assertEqual(self.employment.job_title, test_job_title)
        self.assertEqual(self.employment.start_date, test_start_date)
        self.assertEqual(self.employment.end_date, test_end_date)
        self.assertEqual(self.employment.leave_reason, test_leave_reason)

    def test_employment_duty(self):
        self.assertEqual(self.employment.duties.get().description, test_duty)

    def test_employment_project(self):
        self.assertEqual(self.employment.projects.get().description, test_project)

class DomainsTestCase(TestCase):
    def setUp(self):
        test_owner = User.objects.create_user(username='Unittest_owner', password='muhdummypassword')
        self.domain = Domain.objects.create(owner=test_owner, name=test_domain)
        
    def test_domain(self):
        self.assertEqual(self.domain.name, test_domain)

class ExperienceTestCase(TestCase):
    def setUp(self):
        test_owner = User.objects.create_user(username='Unittest_owner', password='muhdummypassword')
        my_domain = Domain.objects.create(owner=test_owner, name=test_domain)
        self.xp = Experience.objects.create(
            owner=test_owner,
            name=test_experience,
            domain=my_domain
        )

    def test_experience(self):
        self.assertEqual(self.xp.name, test_experience)

class EducationTestCase(TestCase):
    def setUp(self):
        test_owner = User.objects.create_user(username='Unittest_owner', password='muhdummypassword')
        self.edu = Education.objects.create(
            owner=test_owner,
            name=test_edu,
            level=test_edu_level,
            year=test_edu_year
        )

    def test_education(self):
        self.assertEqual(self.edu.name, test_edu)
        self.assertEqual(self.edu.level, test_edu_level)
        self.assertEqual(self.edu.year, test_edu_year)

class ReferenceTestCase(TestCase):
    def setUp(self):
        test_owner = User.objects.create_user(username='Unittest_owner', password='muhdummypassword')
        employer = Employment.objects.create(
            owner=test_owner,
            company_name=test_company_name,
            job_title=test_job_title,
            start_date=test_start_date,
            end_date=test_end_date,
            leave_reason=test_leave_reason,
        )
        self.reference = Reference.objects.create(
            owner=test_owner,
            name=test_ref,
            contact=test_ref_contact,
            employment=employer
        )
        
    def test_reference(self):
        self.assertEqual(self.reference.name, test_ref)
        self.assertEqual(self.reference.contact, test_ref_contact)
        self.assertEqual(self.reference.employment.company_name, test_company_name)
        self.assertEqual(self.reference.employment.leave_reason, test_leave_reason)

class ApplicantTestCase(TestCase):
    def setUp(self):
        test_owner = User.objects.create_user(username='Unittester', password='muhdummypassword')
        self.applicant = Applicant.objects.create(
            name=test_applicant,
            email=test_email,
            phone=test_phone,
            owner=test_owner
        )
        Domain.objects.create(
            owner=test_owner,
            name=test_domain
        )
        my_domain = Domain.objects.get(name=test_domain)
        Experience.objects.create(
            owner=test_owner,
            name=test_experience,
            domain=my_domain
        )
        my_xps = [Experience.objects.get(name=test_experience)]
        
        self.applicant.experiences.set(my_xps)
        Education.objects.create(
            owner=test_owner,
            name=test_edu,
            level=test_edu_level,
            year=test_edu_year
        )
        my_edu = [Education.objects.get(name=test_edu)]
        self.applicant.education.set(my_edu)
        my_emp = [Employment.objects.create(
            owner=test_owner,
            company_name=test_company_name,
            job_title=test_job_title,
            start_date=test_start_date,
            end_date=test_end_date,
            leave_reason=test_leave_reason,
        )]
        my_refs = [Reference.objects.create(
            owner=test_owner,
            name=test_ref,
            contact=test_ref_contact,
            employment=my_emp[0]
        )]
        self.applicant.reference.set(my_refs)
        self.applicant.employment.set(my_emp)

    def test_applicant(self):
        self.assertEqual(self.applicant.name, test_applicant)
        self.assertEqual(self.applicant.email, test_email)
        self.assertEqual(self.applicant.phone, test_phone)

    def test_applicant_experience(self):
        self.assertEqual(self.applicant.experiences.get(name=test_experience).name, test_experience)
        self.assertEqual(self.applicant.experiences.get(name=test_experience).domain.name, test_domain)
        

    def test_applicant_education(self):
        self.assertEqual(self.applicant.education.get(name=test_edu).name, test_edu)

    def test_applicant_reference(self):
        self.assertEqual(self.applicant.reference.get(name=test_ref).name, test_ref)

    def test_applicant_employment(self):
        self.assertEqual(self.applicant.employment.get(company_name=test_company_name).job_title, test_job_title)


class ResumeTestCase(TestCase):
    def setUp(self):
        test_owner = User.objects.create_user(username='Unittest_owner', password='muhdummypassword')
        resume_applicant = Applicant.objects.create(
            owner=test_owner,
            name=test_applicant,
            email=test_email,
            phone=test_phone
        )
        template = Template.objects.create(
            owner=test_owner,
            name=test_template_name,
            file="path_to_test_file.docx"
        )
        self.resume = Resume.objects.create(
            owner=test_owner,
            name=test_resume_name,
            output_format=test_output_format,
            applicant=resume_applicant,
            template=template
        )

    def test_resume(self):
        self.assertEqual(self.resume.name, test_resume_name)
        self.assertEqual(self.resume.output_format, test_output_format)
        self.assertEqual(self.resume.applicant.name, test_applicant)
        self.assertEqual(self.resume.template.name, test_template_name)
        