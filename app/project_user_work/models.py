from django.db import models
from ..user.models import User
from ..project.models import Project

class ProjectUserWork(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    work = models.CharField(max_length=100)
    archieves = models.CharField(max_length=100)