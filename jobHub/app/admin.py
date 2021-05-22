from django.contrib import admin

# Register your models here.
from .models import addJob, Applicant

admin.site.register(addJob)
admin.site.register(Applicant)