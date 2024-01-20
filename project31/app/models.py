from django.db import models
from django.core import validators


# Create your models here.



class Student(models.Model):
    sname=models.CharField(max_length=100)
    sage=models.IntegerField(default=5)
    smobile=models.CharField(max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])

    def __str__(self):
        return self.sname
