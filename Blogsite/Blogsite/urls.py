
from django.contrib import admin
from django.urls import path , include
from Blogs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Blogs.urls')),
    path('', include('meetings.urls')),
]
