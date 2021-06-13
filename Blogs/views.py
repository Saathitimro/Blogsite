from Blogs.models import BlogModel
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {'blogs' : BlogModel.objects.all()}
    return render(request, "Pages/Index.html" , context)

def blog(request):
    context = {'blogs' : BlogModel.objects.all()}
    return render(request, "Pages/Blogs.html", context)

def details(request,pk):
    context = {'blogs' : BlogModel.objects.get(id=pk)}
    return render(request,"Pages/blogpost.html", context)