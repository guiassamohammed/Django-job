from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.

Job_type = (('Full time','Full time'),
('Part time','Part time'),

)

def image_upload(instance, filename):
  imagename, extenstion = filename.split(".")
  return "jobs/%s.%s"%(instance.id,extenstion)

class Job(models.Model):
   owner = models.ForeignKey('auth.User',related_name= 'job_owner',on_delete = models.CASCADE)
   title = models.CharField(max_length=100) 
   job_type = models.CharField(max_length= 50, choices= Job_type)
   Description = models.TextField(max_length= 10000)
   Publushed_at = models.DateField(auto_now= True)
   Vacany = models.IntegerField(default= 1 )
   Salary = models.IntegerField(default = 0)
   Experience = models.IntegerField(default = 1)
   Category = models.ForeignKey('Category', on_delete = models.CASCADE)
   Image = models.ImageField(upload_to = image_upload)

   slug = models.SlugField(blank= True,null= True)

   def save(self,*args,**kwargs): 
      self.slug =  slugify(self.title)
      super(Job,self).save(*args,**kwargs)


   def __str__(self): 
      return self.title


class Category(models.Model):
   name = models.CharField(max_length=  25)

   def __str__(self): 
      return self.name 


class Apply(models.Model): 
   job = models.ForeignKey(Job, related_name= 'apply_job', on_delete =  models.CASCADE )
   name = models.CharField(max_length= 100)
   email = models.EmailField(max_length= 50)
   cv = models.FileField(upload_to= 'apply/')
   web_site = models.URLField()
   cover_letter = models.TextField(max_length= 500)
   created_at = models.DateTimeField(auto_now= True)

   def __str__(self): 
      return self.name 

