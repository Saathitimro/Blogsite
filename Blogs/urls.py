from django.urls import path
from .views import *
from Blogs import views

urlpatterns = [
    path('', views.home),
    path('home', views.home),
    path('blog', views.blog, name="blog-list"),
    path('login', views.login),
    path('profile', views.profile),
    path('schedule', views.schedule),
    path('pending', views.pending),
    path('detail', views.detail),
    path('blog_details/<slug>', views.blog_details, name="blog-details"),
]
