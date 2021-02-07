from django.db import models

# Create your models here.

Job_type = (('Full time','Full time'),
('Part time','Part time'),

)


class Job(models.Model):
   title = models.CharField(max_length=100) 
   job_type = models.CharField(max_length= 50, choices= Job_type)
   Description = models.TextField(max_length= 10000)
   Publushed_at = models.DateField(auto_now= True)
   Vacany = models.IntegerField(default= 1 )
   Salary = models.IntegerField(default = 0)
   Experience = models.IntegerField(default = 1)

   def __str__(self): 
      return self.title