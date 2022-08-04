from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    age = models.IntegerField(default=0)
