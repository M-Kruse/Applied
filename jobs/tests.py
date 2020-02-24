from datetime import datetime

from django.test import TestCase

from django.contrib.auth.models import User

from jobs.models import (Job, JobSite, Description,
                         Aggregator, Application)

from resume.models import Template, Resume, Applicant

test_name = "Rusty Shackleford"
test_email = "rustshack@noreply"
test_phone = "+11234567890"
test_keywords = "django"
test_job_site = "indeed"
test_company = "Bar Corp"
test_title = "Fooperator"
test_location = "Foosville"
test_description = "Come join us as a Fooperator at Bar Corp where you will help make Foo resilient, performant and highly available to the world."
test_post_date = "01-01-2001"
test_scrape_date = "01-01-2020"
test_random_date = datetime.now().strftime("%Y-%m-%d %H:%M")
test_url = "https://www.example.com"
test_availability = True
test_favorite = True
test_hidden = True
test_delete = True
test_search_url_template = "?foo=bar&goodboy=houdino"
test_jobs_per_page = 30
test_page_parameter = "p=1"
test_easy_apply = True
test_max_threads = 99
test_run_schedule = "Manual"
test_archive_html = True
test_send_alerts = True
test_status = "UA"
test_contact = "Johnny Dough"
test_notes = "Application notes like your thoughts at the time, any research you did on the company and any other things to remember about the application"
test_template_name = "Default Template"
test_resume_name = "Rustys Rez"
test_output_format = "DOCX"
test_interview_type = "EM"
test_interview_status = "OF"

class JobTestCase(TestCase):
    def setUp(self):
        test_owner = User.objects.create_user(username='Beavis', password='unit_huhuhuh')
        desc = Description.objects.create(text=test_description)
        self.job = Job.objects.create(
            owner=test_owner,
            keywords=test_keywords,
            job_site=test_job_site,
            title=test_title,
            company=test_company,
            location=test_location,
            description=desc,
            date_posted=test_post_date,
            date_scraped=test_scrape_date,
            url=test_url,
            is_available=test_availability,
            is_favorite=test_favorite,
            is_hidden=test_hidden,
            is_delete=test_delete
        )

    def test_job(self):
        self.assertEqual(self.job.keywords, test_keywords)

class JobSiteTestCase(TestCase):
    def setUp(self):
        test_owner = User.objects.create_user(username='Beavis', password='unit_uhuhuhuh')
        self.job_site = JobSite.objects.create(
            url=test_url,
            search_url_template=test_search_url_template,
            jobs_per_page=test_jobs_per_page,
            page_parameter=test_page_parameter,
            is_easy_apply=test_easy_apply,
            apply_url=test_url
        )

    def test_jobsite(self):
        self.assertEqual(self.job_site.url, test_url)
        self.assertEqual(self.job_site.search_url_template, test_search_url_template)
        self.assertEqual(self.job_site.jobs_per_page, test_jobs_per_page)
        self.assertEqual(self.job_site.page_parameter, test_page_parameter)
        self.assertEqual(self.job_site.is_easy_apply, test_easy_apply)
        self.assertEqual(self.job_site.apply_url, test_url)



class AggregatorTestCase(TestCase):
    def setUp(self):
        test_owner = User.objects.create_user(username='Beavis', password='unit_uhuhuhuh')
        self.job_site = JobSite.objects.create(
            url=test_url,
            search_url_template=test_search_url_template,
            jobs_per_page=test_jobs_per_page,
            page_parameter=test_page_parameter,
            is_easy_apply=test_easy_apply,
            apply_url=test_url
        )
        self.aggregator = Aggregator.objects.create(
            keywords=test_keywords,
            job_site=self.job_site,
            max_threads=test_max_threads,
            run_schedule=test_run_schedule,
            archive_raw_html=test_archive_html,
            send_alerts=test_send_alerts
        )

    def test_aggregator(self):
        self.assertEqual(self.aggregator.keywords, test_keywords)
        self.assertEqual(self.aggregator.job_site, self.job_site)
        self.assertEqual(self.aggregator.max_threads, test_max_threads)
        self.assertEqual(self.aggregator.run_schedule, test_run_schedule)
        self.assertEqual(self.aggregator.archive_raw_html, test_archive_html)
        self.assertEqual(self.aggregator.send_alerts, test_send_alerts)


class ApplicationTestCase(TestCase):
    def setUp(self):
        print(datetime(2001, 12, 1, 1, 0))
        test_owner = User.objects.create_user(username='Beavis', password='unit_uhuhuhuh')
        desc = Description.objects.create(text=test_description)
        self.test_job = Job.objects.create(
            owner=test_owner,
            keywords=test_keywords,
            job_site=test_job_site,
            title=test_title,
            company=test_company,
            location=test_location,
            description=desc,
            date_posted=test_post_date,
            date_scraped=test_scrape_date,
            url=test_url,
            is_available=test_availability,
            is_favorite=test_favorite,
            is_hidden=test_hidden,
            is_delete=test_delete
        )
        test_applicant = Applicant.objects.create(
            owner=test_owner,
            name=test_name,
            email=test_email,
            phone=test_phone
        )
        test_template = Template.objects.create(
            owner=test_owner,
            name=test_template_name,
            file="path_to_test_file.docx"
        )
        self.test_resume = Resume.objects.create(
            owner=test_owner,
            name=test_resume_name,
            output_format=test_output_format,
            applicant=test_applicant,
            template=test_template
        )
        self.application = Application.objects.create(
            create_date=test_random_date,
            apply_date=test_random_date,
            owner=test_owner,
            job=self.test_job,
            status=test_status,
            contact=test_contact,
            notes=test_notes,
            resume=self.test_resume
        )

    def test_application(self):
        self.assertEqual(self.application.create_date.strftime("%Y-%m-%d %H:%M"), test_random_date)
        self.assertEqual(self.application.apply_date, test_random_date)
        self.assertEqual(self.application.job, self.test_job)
        self.assertEqual(self.application.status, test_status)
        self.assertEqual(self.application.contact, test_contact)
        self.assertEqual(self.application.notes, test_notes)
        self.assertEqual(self.application.resume, self.test_resume)


def InterviewTestCase(TestCase):
    def setUp(self):
        test_owner = User.objects.create_user(username='Beavis', password='unit_uhuhuhuh')
        self.test_job = Job.objects.create(
            owner=test_owner,
            keywords=test_keywords,
            job_site=test_job_site,
            title=test_title,
            company=test_company,
            location=test_location,
            description=desc,
            date_posted=test_post_date,
            date_scraped=test_scrape_date,
            url=test_url,
            is_available=test_availability,
            is_favorite=test_favorite,
            is_hidden=test_hidden,
            is_delete=test_delete
        )
        test_applicant = Applicant.objects.create(
            owner=test_owner,
            name=test_name,
            email=test_email,
            phone=test_phone
        )
        test_template = Template.objects.create(
            owner=test_owner,
            name=test_template_name,
            file="path_to_test_file.docx"
        )
        self.test_resume = Resume.objects.create(
            owner=test_owner,
            name=test_resume_name,
            output_format=test_output_format,
            applicant=test_applicant,
            template=test_template
        )
        self.application = Application.objects.create(
            create_date=test_random_date,
            apply_date=test_random_date,
            owner=test_owner,
            job=self.test_job,
            status=test_status,
            contact=test_contact,
            notes=test_notes,
            resume=self.test_resume
        )
        self.interview = Interview.objects.create(
            owner=test_owner,
            application=self.application,
            date=test_random_date,
            type=test_interview_type,
            contact=test_contact,
            notes=test_notes,
            date_created=test_random_date,
            status=test_interview_status
        )

    def test_interview(self):
        self.assertEqual(self.interview.application, self.application)
        self.assertEqual(self.interview.date, test_random_date)
        self.assertEqual(self.interview.type, test_interview_type)
        self.assertEqual(self.interview.contact, test_contact)
        self.assertEqual(self.interview.notes, test_notes)
        self.assertEqual(self.interview.date_created, test_random_date)
        self.assertEqual(self.interview.status, test_interview_status)


