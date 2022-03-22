from django.db import models

class UserRolePermission(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=100)
    role_id = models.IntegerField()
    role_name = models.CharField(max_length=100)
    permission_id = models.IntegerField()
    permission_codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "user_role_permission"
        # indexes = [
        #     models.Index(fields=['username',]),
        #     models.Index(fields=['role_name','permission_codename',]),
        # ]
