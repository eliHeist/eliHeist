from django.conf.urls import url
from django.db import models

# Create your models here.
class Project(models.Model):
   name = models.CharField(max_length=20)
   thumbnail = models.ImageField()
   link = models.CharField(max_length=1080)

   def __str__(self):
        return self.name