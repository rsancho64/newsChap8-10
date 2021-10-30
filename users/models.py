from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser # not AbstractBaseUser !!

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)