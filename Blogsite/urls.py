
from django.contrib import admin
from django.urls import path
from Blogs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('home', views.home),
    path('blog', views.blog),
    path('details', views.details),
]
