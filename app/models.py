import datetime

from django.db import models
from django.contrib.auth.models import User, AbstractUser

class User(AbstractUser):
    position = models.CharField(max_length=100)
    rank = models.CharField(max_length=100)
    def __str__(self):
        return self.username

class GroupSkill(models.Model):
    group_skill_name = models.CharField(max_length=100)
    def __str__(self):
        return self.group_skill_name

class Skill(models.Model):
    skill_name = models.CharField(max_length=100)
    group_skill_id = models.ForeignKey(GroupSkill, on_delete=models.CASCADE)
    def __str__(self):
        return self.skill_name

class UserSkill(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE)
    year_of_experience = models.IntegerField(blank=True, null=True)
    level = models.CharField(max_length=100 ,blank=True, null=True)

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date_start = models.DateField()
    date_end = models.DateField()
    tech_stack = models.CharField(max_length=100)
    def __str__(self):
        return self.project_name

class ProjectUserWork(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    work = models.CharField(max_length=100)
    archieves = models.CharField(max_length=100)

class Rating(models.Model):
    user_id_rated = models.ForeignKey(User, on_delete=models.CASCADE)
    session_rating = models.DateField()

class DetailRating(models.Model):
    user_id_assessor = models.ForeignKey(User, on_delete=models.CASCADE)
    rating_id = models.ForeignKey(Rating, on_delete=models.CASCADE)
    score = models.IntegerField()
    description = models.TextField(blank=True, null=True)

class LogRating(models.Model):
    detail_rating_id = models.ForeignKey(DetailRating, on_delete=models.CASCADE)
    update_at = models.DateTimeField()
