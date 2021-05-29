from django.db import models

# Create your models here.

class Seminar(models.Model):
    Name = models.CharField(max_length=50)
    email = models.EmailField(max_length = 254)
    age = models.CharField(max_length=10,null=True)
    sex = models.CharField(null=True, max_length=10)


class Meeting(models.Model):
    topic = models.CharField(max_length=50)
    url = models.TextField(max_length = 254)
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
