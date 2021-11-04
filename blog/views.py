from django.shortcuts import render
from django.views.generic import ListView

from blog.models import Post

# Create your views here.
class BlogList(ListView):
   model = Post
   context_object_name='posts'
   template_name = 'blog/blog-list.html'