from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/%d/%m/%Y', blank=True)
    description = models.TextField()
    hability = models.CharField(max_length=150)



