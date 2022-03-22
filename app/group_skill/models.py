from django.db import models

class GroupSkill(models.Model):
    group_skill_name = models.CharField(max_length=100)
    class Meta:
        db_table = "group_skill"    
    def __str__(self):
        return self.group_skill_name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    group_skill_id = models.ForeignKey(GroupSkill, on_delete=models.CASCADE)

    class Meta:
        db_table = "skill"
    def __str__(self):
        return self.skill_name