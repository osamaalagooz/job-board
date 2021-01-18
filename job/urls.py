
from django.urls import path
from .views import job_apply, job_details, jobs, add_job, like_btn

urlpatterns = [
    path('', jobs, name = "job_list"),
    path('<int:id>', job_details, name='job_details'),
    path('addJob', add_job, name='jobEditor'),
    path('<int:id>/like', like_btn, name='like'),
    path('<int:id>/apply', job_apply, name='application'),
]

app_name = 'job'