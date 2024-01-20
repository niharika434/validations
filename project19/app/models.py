from django.db import models

# Create your models here.
class Dept(models.Model):
    dept_no=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)

    def __str__(self):
        return self.name
   

class Emp(models.Model):
    emp_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    sal=models.IntegerField()
    hire_date=models.DateField()
    dept_no=models.OneToOneField(Dept,on_delete=models.CASCADE)

    def __str__(self):
        return self.name