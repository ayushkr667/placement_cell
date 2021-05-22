from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('dashboard/applicants/<int:id>', views.applicants, name = 'applicants'),
    path('dashboard/delete_job/<int:id>/', views.delete_job, name = 'delete_job'),
    path('dashboard/applicants/reject/<int:id>/<int:job_id>', views.reject_applicant, name = 'reject_applicant'),
    path('add_vacancy/', views.add_vacancy, name = 'add_vacancy'),
    path('apply_job/<int:id>', views.apply_job, name = 'apply_job'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('signup/', views.signup, name = 'signup'),
    path('signin/', views.signin, name = 'signin'),
    path('signout/', views.signout, name = 'signout'),
]