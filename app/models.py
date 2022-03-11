from .user.models import User
from .group_skill.models import GroupSkill, Skill
from .user_skill.models import UserSkill
from .project.models import Project
from .project_user_work.models import ProjectUserWork
from .rating.models import Rating, DetailRating, LogRating
from django.db import models

class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, db_column='created_at', blank=True, null=True,
                                      verbose_name=('Created at'))
    updated_at = models.DateTimeField(auto_now=True, db_column='modified_at', blank=True, null=True,
                                      verbose_name=('Updated at'))
    created_by = models.CharField(max_length=100, db_column='created_by', blank=True, null=True, default='',
                                  verbose_name=('Created by'))
    updated_by = models.CharField(max_length=100, db_column='modified_by', blank=True, null=True, default='',
                                  verbose_name=('Updated by'))

    server_file_url = None
    server_avatar_url = None
    server_image_url = None

    class Meta:
        abstract = True
