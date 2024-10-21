from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

# Optionally add a custom user model if you want to store phone numbers or other fields
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=50, unique=True)
