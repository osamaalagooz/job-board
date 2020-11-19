from django.db import models

# Create your models here.
JOB_CHOICES = (
    ("Part Time","Part Time"),
    ("Full Time", "Full Time"),
)

# customize imges name on the file system.
def upload_image(instance, filename):
    extension = filename.split('.')[1]
    return 'jobs/%s.%s'%(instance.title, extension)

class Job(models.Model):
    title = models.CharField(max_length = 150)
    description = models.TextField(max_length = 1000)
    author = models.CharField(max_length= 50)
    job_type = models.CharField(max_length = 150, choices=JOB_CHOICES)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=1)
    experience = models.IntegerField(default=1)
    image = models.ImageField(upload_to=upload_image)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return self.title


class Category(models.Model):
    """Model definition for MODELNAME."""

    # TODO: Define fields here
    name = models.CharField(max_length = 150)

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length = 150)
    email = models.EmailField(max_length=100)
    website = models.URLField(max_length = 300)
    cv = models.FileField(upload_to='CVs/', max_length = 100)
    cover_letter = models.TextField()

    def __str__(self):

        return self.name
    
    

    
            
   
    
    

    