from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def ads(request):
    return render(request, 'app-ads.txt')