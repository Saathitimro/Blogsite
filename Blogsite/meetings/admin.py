from django.contrib import admin

# Register your models here.
from .models import Seminar,Meeting

admin.site.register(Seminar)
admin.site.register(Meeting)
