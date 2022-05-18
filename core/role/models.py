from django.db import models
# from ..user.models import User
from rating_employee import settings
class Role(models.Model):
    name = models.CharField(max_length=100)
    priority = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, db_column='created_at', blank=True, null=True,
                                      verbose_name=('Created at'))
    updated_at = models.DateTimeField(auto_now=True, db_column='modified_at', blank=True, null=True,
                                      verbose_name=('Updated at'))
    created_by = models.CharField(max_length=100, db_column='created_by', blank=True, null=True, default='',
                                  verbose_name=('Created by'))
    updated_by = models.CharField(max_length=100, db_column='modified_by', blank=True, null=True, default='',
                                  verbose_name=('Updated by'))
    
    class Meta:
        db_table = "role"

class UserRole(models.Model):

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_id")
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="role_id")

    created_at = models.DateTimeField(auto_now_add=True, db_column='created_at', blank=True, null=True,
                                      verbose_name=('Created at'))
    updated_at = models.DateTimeField(auto_now=True, db_column='modified_at', blank=True, null=True,
                                      verbose_name=('Updated at'))
    created_by = models.CharField(max_length=100, db_column='created_by', blank=True, null=True, default='',
                                  verbose_name=('Created by'))
    updated_by = models.CharField(max_length=100, db_column='modified_by', blank=True, null=True, default='',
                                  verbose_name=('Updated by'))
    class Meta:
        db_table = "user_role"