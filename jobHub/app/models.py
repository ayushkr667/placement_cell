from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

jobType_choices = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)

class addJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_Name = models.CharField(max_length = 100)
    title = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=200)
    jobType = models.CharField(choices = jobType_choices, max_length=2)
    created_on = models.DateTimeField(default = timezone.now)
    last_date = models.DateTimeField()
    salary = models.IntegerField()
    # filled = models.BooleanField(default = False)

    def __str__(self):
        return self.title


class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    job = models.ForeignKey(addJob, on_delete = models.CASCADE, related_name = 'applicants')
    applied_on = models.DateTimeField(default = timezone.now)
    Full_name = models.CharField(max_length=100)
    phone_no = models.IntegerField(blank=False)
    college = models.CharField(max_length=200, blank=False)
    graduation_year = models.IntegerField()
    resume_link = models.URLField(max_length = 200)

    def __str__(self):
        return self.Full_name


