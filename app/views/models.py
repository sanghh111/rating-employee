from django.db import models
from dbview.models import DbView

class Temp_UserRolePermission(DbView):
    count = models.IntegerField()