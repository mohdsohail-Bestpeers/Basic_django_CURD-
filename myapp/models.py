from django.db import models

from django.contrib.auth.models import User


class Blog(models.Model):
    name = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=200)
    blog = models.TextField()



