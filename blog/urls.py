from django.urls import path

from blog.views import BlogList

app_name = 'blog'

urlpatterns = [
   path('', BlogList.as_view(), name='blog-list'),
]