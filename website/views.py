from django.shortcuts import render
from .models import Product, Blog, Comment, Fanbase

def home(request):
    return render(request, 'home.html', {'products':Product.objects.all, 'fanbase':Fanbase.objects.all(), 'blogs':Blog.objects.all()})

def ads(request):
    return render(request, 'app-ads.txt')