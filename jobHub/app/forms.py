from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import addJob, Applicant

class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Retype password'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name' , 'email', 'password1', 'password2']
        labels = {'email': 'Email'}

        widgets = {
            'username' : forms.TextInput({'placeholder': 'Username'}),
            'first_name' : forms.TextInput({'placeholder': 'Firstname'}),
            'last_name' : forms.TextInput({'placeholder': 'Lastname'}),
            'email' : forms.EmailInput({'placeholder': 'E-mail'}),
        }




class CreateJobForm(ModelForm):
    class Meta:
        model = addJob
        exclude = ['user' , 'created_on',]


class JobApplyForm(ModelForm):
    class Meta:
        model = Applicant
        fields = ['Full_name', 'phone_no', 'college', 'graduation_year', 'resume_link']
