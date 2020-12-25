
from django.urls import path
from .views import job_details, jobs, add_job, like_btn

urlpatterns = [
    path('', jobs, name = "job_list"),
    path('<int:id>', job_details, name='job_details'),
    path('addJob', add_job, name='jobEditor'),
    path('<int:id>/like', like_btn, name='like'),
    # path('<int:id>/dislike', disLiker, name='dislike'),
]

app_name = 'job'