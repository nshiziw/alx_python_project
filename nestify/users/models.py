from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('property_owner', 'Property Owner'),
        ('admin', 'Admin'),
    )
    usertype = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='property_owner')