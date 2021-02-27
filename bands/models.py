from django.db import models

class Band(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    style = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
