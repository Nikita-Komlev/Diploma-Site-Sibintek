from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    company = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
