from django.contrib.auth.models import Permission
from ..role.models import Role
from django.db import models

class RolePermission(models.Model):
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission_id = models.ForeignKey(Permission, on_delete=models.CASCADE)

