from django.db import models
from ..user.models import User
from ..group_skill.models import Skill

class UserSkill(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE)
    year_of_experience = models.IntegerField(blank=True, null=True)
    level = models.CharField(max_length=100 ,blank=True, null=True)

    class Meta:
        db_table = "user_skill"