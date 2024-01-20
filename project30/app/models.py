from django.db import models

# Create your models here.
class School(models.Model):
    sname=models.CharField(max_length=100)
    sloc=models.CharField(max_length=100)
    sprince=models.CharField(max_length=100)
    email=models.EmailField()
    re_enter=models.EmailField()

    def __str__(self):
        return self.sname