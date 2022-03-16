from django.db import models
from ..models import User
class Role(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=255, blank=True, null=True)

class UserRole(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
