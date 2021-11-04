from django.shortcuts import render
from django.urls.conf import include
from django.views.generic import ListView

from projects.models import Project

# Create your views here.
class ProjectList(ListView):
   model = Project
   context_object_name = 'projects'
   template_name = 'projects/project-list.html'
   