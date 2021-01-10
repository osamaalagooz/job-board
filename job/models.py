from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.conf import settings
from taggit.managers import TaggableManager
# Create your models here.
JOB_CHOICES = (
    ("Part Time","Part Time"),
    ("Full Time", "Full Time"),
)

# customize imges name on the file system.
def upload_to(instance, filename, path):
    extension = filename.split('.')[1]
    if instance.title:
        return path + '%s.%s'%(instance.title, extension)
    else:
        return path + '%s.%s'%(instance.name, extension)
# def upload_cv(instance, filename):
#     extension = filename.split('.')[1]
#     return 'candidaties/cvs/%s.%s'%(instance.name, extension)
class Job(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 150)
    #description = models.TextField(max_length = 1000)
    description = RichTextField(blank=True, null=True)
    company = models.CharField(max_length= 50)
    job_type = models.CharField(max_length = 150, choices=JOB_CHOICES)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=1)
    experience = models.IntegerField(default=1)
    image = models.ImageField(upload_to=upload_to(path='images/jobs/'))
    likes_num = models.IntegerField()
    likers = models.ManyToManyField(User, related_name='liked_jobs')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    objects = models.Manager()
    tags = TaggableManager()

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return self.title


class Category(models.Model):
    """Model definition for MODELNAME."""

    name = models.CharField(max_length = 150)

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to=upload_to(path='images/companies/'))
    employee_num = models.IntegerField(default=0)
    description = RichTextField(blank=True, null=True)
    user =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        """Unicode representation of MODELNAME."""
        return self.name


class Employee(models.Model):

    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length = 150)
    email = models.EmailField(max_length=100)
    website = models.URLField(max_length = 300)
    cv = models.FileField(upload_to=upload_to(path='cvs/candidaties/'))
    cover_letter = RichTextField(blank=True, null=True)
    job = models.ForeignKey('Job', on_delete=models.CASCADE)
    objects = models.Manager()
    skills = TaggableManager()

    def __str__(self):

        return self.name
    
    

    
            
    
    

    