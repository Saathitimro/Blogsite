from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "Pages/Index.html")

def blog(request):
    return render(request, "Pages/Blogs.html")

def details(request):
    return render(request,"Pages/blogpost.html")