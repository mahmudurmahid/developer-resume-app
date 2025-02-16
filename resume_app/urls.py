from . import views
from django.urls import path
from .views import upload_resume, submit_job_description

urlpatterns = [
    path('', 
        views.HomePage.as_view(), name='home'),
    path('upload/', upload_resume, name='upload_resume'),
    path('job-description/', submit_job_description, name='submit_job_description'),
]
