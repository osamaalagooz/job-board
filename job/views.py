from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Job
from .forms import EmployeeForm, JobForm
from django.urls import reverse 
from django.contrib.auth.decorators import login_required
from .filters import JobFilter

# Create your views here.
def jobs(request):

    jobs_list = Job.objects.all()
    my_filter = JobFilter(data=request.GET, queryset=jobs_list)
    jobs_list = my_filter.qs

    paginator = Paginator(jobs_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "jobs_list": page_obj,
        'my_filter': my_filter
    }
    return render(request, "job/job_list.html", context)

def job_details (request, id):

    job_details = Job.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.job = job_details
            my_form.save()
    
    else:
        form = EmployeeForm()

    context = {
        "job_details": job_details,
        "form": form,
    }
    return render(request, "job/job_details.html", context)
    
@login_required
def add_job(request):
    if request.method == "POST":
        form = JobForm(request.POST, request.FILES)
        if form.is_valid:
            myForm = form.save(commit=False)
            myForm.owner = request.user
            myForm.save()
            return redirect(reverse("jobs:job_list"))
    else:
        form = JobForm()     

    context = {
        "jobForm": form,
    }       
    
    return render(request, "job/add_job.html", context)

@login_required
def like_btn(request, id):
    
    job = Job.objects.get(id=id)

    if request.user not in job.likers.all():
        job.likers.add(request.user)
        return JsonResponse({
        'status': 'ok',
        "message": "like"
    })
    job.likers.remove(request.user)
    
    return JsonResponse({
        'status': 'ok',
        "message": "dislike"
    })
    