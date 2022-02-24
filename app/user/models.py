from django.contrib.auth.models import User, AbstractUser
from django.db import models

class User(AbstractUser):
    position = models.CharField(max_length=100)
    rank = models.CharField(max_length=100)
    def __str__(self):
        return self.username
