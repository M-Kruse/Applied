from django.forms import ModelForm
from jobs.models import JobSite, Aggregator, Application, Interview
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django import forms

class JobSiteForm(ModelForm):
	class Meta:
		model = JobSite
		fields = ['url', 'search_url_template', 'jobs_per_page', 'page_parameter' ]

class AggregatorForm(ModelForm):
	class Meta:
		model = Aggregator
		fields = ['job_site', 'keywords', 'run_schedule', 'archive_raw_html', 'send_alerts', 'max_threads' ]

class ApplicationForm(ModelForm):
	class Meta:
		model = Application
		fields = ['apply_date', 'job', 'status', 'contact', 'notes' ]

class InterviewForm(ModelForm):
	class Meta:
		model = Interview
		fields = ['application', 'date', 'type', 'contact', 'notes', 'status' ]
