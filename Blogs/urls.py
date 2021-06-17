from django.urls import path
from .views import *
from Blogs import views

urlpatterns = [
    path('', views.home),
    path('home', views.home),
    path('blog', views.blog),
    path('login', views.login),
    path('profile', views.profile),
    path('schedule', views.schedule),
    path('pending', views.pending),
    path('detail', views.detail),
    path('<pk>/details/', views.details),
]
