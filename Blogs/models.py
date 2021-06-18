from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField



class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    summery = models.TextField()
    content = FroalaField()
    image = models.ImageField(upload_to='static/img')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
