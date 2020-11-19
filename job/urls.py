



from django.urls import path
from .views import job_details, jobs

urlpatterns = [
    path('', jobs),
    path('<int:id>', job_details, name='job_details'),
]

app_name = 'job'