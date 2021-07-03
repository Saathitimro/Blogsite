from Blogs.models import BlogModel
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {'blogs' : BlogModel.objects.all()}
    return render(request, "Pages/Index.html" , context)

def login(request):
    return render(request, "Pages/counselor/login.html")

def blog(request):
    context = {'blogs' : BlogModel.objects.all()}
    return render(request, "Pages/Blogs.html", context)

def blog_details(request, slug):
    context = {}
    try:
        blogs = BlogModel.objects.filter(slug = slug).first()
        context['blogs'] = blogs
    except Exception as e:
        print(e)
    return render(request,"Pages/blogdetail.html")

def profile(request):
    return render(request, "Pages/counselor/profile.html")

def detail(request):
    return render(request, "Pages/counselor/detail.html")

def pending(request):
    return render(request, "Pages/counselor/pending.html")

def schedule(request):
    return render(request, "Pages/counselor/schedule.html")