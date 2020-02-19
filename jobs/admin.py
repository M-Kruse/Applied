from django.contrib import admin
from .models import Job, JobSite, Aggregator, Application
# Register your models here.
admin.site.register(Job)
admin.site.register(JobSite)
admin.site.register(Aggregator)
admin.site.register(Application)

