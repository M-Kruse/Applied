from django.db import models

class Application(models.Model):
    self.STATUS_CHOICES = ["UNAPPLIED", "APPLIED", "INTERVIEWING", "DECLINED"]
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    apply_date = models.DateTimeField()
    owner = models.ForeignKey('auth.User', related_name='owner', on_delete=models.PROTECT)
    job = models.ForeignKey('Job', related_name='job', on_delete=models.PROTECT)
    status = models.CharField(choices=self.STATUS_CHOICES, max_length=12, default='')
    contact = models.CharField(max_length=100, default='')
    notes = models.TextField()


class Interview(models.Model):
    self.TYPE = ["Email", "Phone", "Video", "In-Person"]
    self.STATUS_CHOICES = ["OFFERED", "SCHEDULED", "COMPLETED"]
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    interview_date = models.DateTimeField()
    owner = models.ForeignKey('auth.User', related_name='owner', on_delete=models.PROTECT)
    job = models.ForeignKey('Job', related_name='job', on_delete=models.PROTECT)
    application = models.ForeignKey('Application', related_name='application', on_delete=models.PROTECT)
    contact = models.CharField(max_length=100, default='')
    notes = models.TextField()