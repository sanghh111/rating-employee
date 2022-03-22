from django.db import models
from ..user.models import User

class Role(models.Model):
    name = models.CharField(max_length=100)
    priority = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = "role"

class UserRole(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_id")
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="role_id")
    class Meta:
        db_table = "user_role"