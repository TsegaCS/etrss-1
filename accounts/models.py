from django.db import models

from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    organization=models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True,blank=True)
    city = models.CharField(max_length=255, null=True,blank=True)
    department = models.CharField(max_length=255, null=True,blank=True)
    email = models.CharField(max_length=255,null=True, blank=True)
    # email = models.EmailField(unique=True, max_length=255,null=True, blank=True)
    address = models.CharField(max_length=255,null=True, blank=True)
    phone = models.CharField(max_length=255,null=True, blank=True)
    def __str__(self):
        return self.organization
