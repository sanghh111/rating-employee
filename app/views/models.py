from django.db import models
from dbview.models import DbView

class UserRolePermission(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=100)
    role_id = models.IntegerField()
    role_name = models.CharField(max_length=100)
    permission_id = models.IntegerField()
    permission_codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "UserRolePermission"