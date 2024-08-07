from django.shortcuts import render
from .models import Blog, Comment, Fanbase

def home(request):
    fanbase = Fanbase.objects.all
    blogs = Blog.objects.all
    return render(request, 'home.html', {'fanbase':fanbase, 'blogs':blogs})

def ads(request):
    return render(request, 'app-ads.txt')

def blog(request, blogId):
    blog = Blog.objects.get(blogId)
    comments = Comment.objects.filter(blog=blog)
    return render(request, 'blog.html', {'blog':blog, 'comments':comments})