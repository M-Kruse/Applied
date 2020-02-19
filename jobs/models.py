from django.db import models
import uuid
from django.conf import settings
from resume.models import Resume
from requests import get

class JobSite(models.Model):
    url = models.CharField(max_length=100, default='', unique=True)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    search_url_template = models.CharField(max_length=100, default='')
    jobs_per_page = models.CharField(max_length=100, default='')
    page_parameter = models.CharField(max_length=100, default='')
    is_easy_apply = models.BooleanField(default=False)
    apply_url = models.CharField(max_length=256, default='')

    def __str__(self):
        return self.url

class Job(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    keywords = models.CharField(max_length=128, default='')
    #job_site = models.ForeignKey(JobSite, on_delete=models.PROTECT)
    job_site = models.CharField(max_length=100, default='')
    title = models.CharField(max_length=100, default='')
    company = models.CharField(max_length=100, default='')
    location = models.CharField(max_length=100, blank=True, default='')
    date_posted = models.CharField(max_length=64, blank=True, default='')
    date_scraped = models.DateTimeField(auto_now_add=True, editable=False)
    url = models.CharField(max_length=512, unique=True, default=uuid.uuid1)
    is_available = models.BooleanField(default=True)
    is_applied = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    description = models.ForeignKey('Description', on_delete=models.CASCADE, blank=True, null=True)

    def save(self, *args, **kwargs):
        super(Job, self).save(*args, **kwargs)

        class Meta:
            ordering = ['date_scraped']

    def __str__(self):
        return "{0} @ {1}".format(self.title, self.company)

class Description(models.Model):
    desc = models.TextField()

class Aggregator(models.Model):
    SCHEDULE_CHOICES = ["Manual", "Hourly", "Daily", "Weekly"]
    keywords = models.CharField(max_length=128, default='')
    job_site = models.ForeignKey(JobSite, on_delete=models.CASCADE)
    max_threads = models.CharField(max_length=100, default='')
    run_schedule = models.CharField(max_length=100, default="Manual")
    archive_raw_html = models.BooleanField(default=False)
    send_alerts = models.BooleanField(default=False)

    def __str__(self):
        return self.job_site.__str__()


class Application(models.Model):
    UNAPPLIED = "UA"
    APPLIED = "AP"
    INTERVIEWING = "IV"
    DECLINED = "DC"
    OFFER = "OF"
    STATUS_CHOICES = [
        (UNAPPLIED, "Unapplied"),
        (APPLIED, "Applied"),
        (INTERVIEWING, "Interviewing"),
        (DECLINED, "Declined"),
        (OFFER, "Offer"),
    ]
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    apply_date = models.DateTimeField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=12, default='')
    contact = models.CharField(max_length=100, default='')
    notes = models.TextField()
    resume = models.ForeignKey(Resume, on_delete=models.PROTECT, default='')


    def __str__(self):
        return "{0} @ {1}".format(self.job.__str__(), self.job.company.__str__())

class Interview(models.Model):
    EMAIL = "EM"
    PHONE = "PH"
    VIDEO = "VD"
    PERSON = "PS"
    TYPE = [
        (EMAIL, "Email"),
        (PHONE, "Phone"),
        (VIDEO, "Video"),
        (PERSON, "In-Person"),
    ]
    OFFERED = "OF"
    SCHEDULED = "SC"
    COMPLETED = "CL"
    STATUS_CHOICES = [
        (OFFERED, "OFFERED"),
        (SCHEDULED, "SCHEDULED"),
        (COMPLETED, "COMPLETED")
    ]
    owner = models.ForeignKey('auth.User', related_name='interview_owner', on_delete=models.PROTECT, blank=True, null=True)
    application = models.ForeignKey('Application', related_name='application', on_delete=models.PROTECT)
    date = models.DateTimeField()
    type = models.CharField(max_length=100, choices=TYPE, default='')
    contact = models.CharField(max_length=100, default='')
    notes = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    status = models.CharField(choices=STATUS_CHOICES, max_length=12, default='')

    def __str__(self):
        return self.application.__str__()