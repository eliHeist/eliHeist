from django.urls import path

from projects.views import ProjectList

app_name = 'projects'

urlpatterns = [
   path('', ProjectList.as_view(), name='project-list'),
]