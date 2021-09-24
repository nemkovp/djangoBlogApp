from django.db import models
from django.utils import timezone


class Post(models.Model):
    name = models.CharField(max_length=30,unique=True)
    author = models.CharField(max_length=300)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    category = models.CharField(max_length=30)
    datas = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name