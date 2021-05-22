from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, CreateJobForm, JobApplyForm
from django.contrib.auth.decorators import login_required
from . models import addJob, Applicant

# home view.
def home(request):
    allJobs = addJob.objects.all().order_by('-created_on')
    context = {
        "all_Jobs" : allJobs 
    }
    return render(request, 'jobHub/home.html', context)


#dashboard view
@login_required(login_url = 'signin')
def dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        createdJobs = addJob.objects.filter(user = user).order_by('created_on')
        context = {
            "createdJobs" : createdJobs 
        }
        return render(request, 'jobHub/employer/dashboard.html', context)


# applicants in dashboard view
@login_required(login_url = 'signin')
def applicants(request, id):
    if request.user.is_authenticated:
        user = request.user
        job = addJob.objects.get(pk = id)
        applicants_for_the_job = Applicant.objects.filter(job = job)
        context = {
            'applicants' : applicants_for_the_job
        }
        return render(request, 'jobHub/employer/applicants.html', context = context)

# reject applicant application view
@login_required(login_url = 'signin')
def reject_applicant(request, id, job_id):
    if request.user.is_authenticated:
        Applicant.objects.get(pk = id).delete()
        job = addJob.objects.get(pk = job_id)
        applicants_for_the_job = Applicant.objects.filter(job = job)
        context = {
            'applicants' : applicants_for_the_job
        }
        return render(request, 'jobHub/employer/applicants.html', context = context)


# delete job in dashboard view
@login_required(login_url = 'signin')
def delete_job(request, id):
    addJob.objects.get(pk = id).delete()
    return redirect('dashboard')


# add a job view
@login_required(login_url = 'signin')
def add_vacancy(request):
    if request.user.is_authenticated:
        user = request.user
        form = CreateJobForm(request.POST)

        if form.is_valid():
            jobDetails = form.save(commit = False)
            jobDetails.user = user
            jobDetails.save()
            return redirect('add_vacancy')

        else:
            form = CreateJobForm()
            context = {
                'form' : form
            }
            return render(request, 'jobHub/employer/addVacancy.html', context)

    else:
        return redirect('signin')


# apply for job view
@login_required(login_url = 'signin')
def apply_job(request, id):
    if request.user.is_authenticated:
        user = request.user
        Job = addJob.objects.get(pk = id)
        form = JobApplyForm(request.POST)

        if form.is_valid():
            applicant = form.save(commit = False)
            applicant.user = user
            applicant.job = Job
            applicant.save()
            return redirect('home')

        else:
            form = JobApplyForm()
            # checking if user is applied already
            applicant = Applicant.objects.filter(job = Job).filter(user = user)
            context = {
                'form' : form,
                'applied' : applicant,
                'job' : Job
            }
            return render(request, 'jobHub/employee/applyJob.html', context)

    else:
        return redirect('signin')    


# about view
def about(request):
    return render(request, 'jobHub/aboutUs.html')


# contact us view
def contact(request):
    return render(request, 'jobHub/contactUs.html')


# signup view
def signup(request):
    if request.method == 'GET':
        form = CreateUserForm()
        context = {
            'form' : form
        }
        return render(request, 'jobHub/signup.html', context = context)
    
    else:
        form = CreateUserForm(request.POST)
        context = {
            'form' : form
        }
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('signin')
            else:
                 return render(request, 'jobHub/signup.html', context = context) 
        else:
            return render(request, 'jobHub/signup.html', context = context)


# signin view
def signin(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            "form" : form
        }
        return render(request, 'jobhub/signin.html', context = context)

    else:
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'jobhub/signin.html', context = context)
        else:
            context = {
                "form" : form
            }
            return render(request, 'jobHub/signin.html', context = context)
            

#signout view
@login_required(login_url = 'signin')
def signout(request):
    logout(request)
    return redirect('home')
