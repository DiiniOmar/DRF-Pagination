from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_number = models.IntegerField()
    emp_name= models.CharField(max_length= 60)
    emp_salary = models.FloatField()
    emp_email = models.EmailField()
    emp_address = models.CharField(max_length= 165)
   