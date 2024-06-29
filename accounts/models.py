from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    usertype = models.CharField(max_length=25)

    def __str__(self):
        return self.username
