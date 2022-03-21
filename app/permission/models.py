from django.contrib.auth.models import Permission
from app.role.models import Role
from django.db import models

class RolePermission(models.Model):
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)

    permission_id = models.ForeignKey(Permission, on_delete=models.CASCADE)

    # created_at = models.DateTimeField(auto_now_add=True, db_column='created_at', blank=True, null=True,
    #                                   verbose_name=('Created at'))
    # updated_at = models.DateTimeField(auto_now=True, db_column='modified_at', blank=True, null=True,
    #                                   verbose_name=('Updated at'))
    # created_by = models.CharField(max_length=100, db_column='created_by', blank=True, null=True, default='',
    #                               verbose_name=('Created by'))
    # updated_by = models.CharField(max_length=100, db_column='modified_by', blank=True, null=True, default='',
    #                               verbose_name=('Updated by'))
