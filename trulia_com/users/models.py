from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=255,default='')
    role = models.CharField(max_length=50,default='USER')
    def __str__(self) -> str:
        return self.user.username
