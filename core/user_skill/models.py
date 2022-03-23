from django.db import models
from ..user.models import User
from ..group_skill.models import Skill

class UserSkill(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE)
    year_of_experience = models.IntegerField(blank=True, null=True)
    level = models.CharField(max_length=100 ,blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, db_column='created_at', blank=True, null=True,
                                      verbose_name=('Created at'))
    updated_at = models.DateTimeField(auto_now=True, db_column='modified_at', blank=True, null=True,
                                      verbose_name=('Updated at'))
    created_by = models.CharField(max_length=100, db_column='created_by', blank=True, null=True, default='',
                                  verbose_name=('Created by'))
    updated_by = models.CharField(max_length=100, db_column='modified_by', blank=True, null=True, default='',
                                  verbose_name=('Updated by'))

    class Meta:
        db_table = "user_skill"