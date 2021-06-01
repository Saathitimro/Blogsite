from django.urls import path
from .views import *
from Blogs import views

urlpatterns = [
    path('', views.home),
    path('home', views.home),
    path('blog', views.blog),
    path('details', views.details),
]
