from rest_framework import serializers
from models import User, Skill, UserSkill, GroupSkill, ProjectUserWork, Project, Rating, LogRating, DetailRating

#class UserSerializer(serializers.Serializer):

class SkillSerializer(serializers.Serializer):
    skill_name = serializers.CharField(max_length=200)
    group_skill_id = serializers.IntegerField()

class GroupSkillSerializer(serializers.Serializer):
    group_skill_name = serializers.CharField(max_length=200)

class UserSkillSerializer(serializers.Serializer):
    skill_id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    year_of_experience = serializers.IntegerField()
    level = serializers.CharField(max_length=200)

class ProjectSerializer(serializers.Serializer):
    project_name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    date_start = serializers.DateField()
    date_end = serializers.DateField()
    tech_stack = serializers.CharField(max_length=200)

class ProjectUserWorkSerializer(serializers.Serializer):
    project_id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    position = serializers.CharField(max_length=200)
    work = serializers.CharField(max_length=200)
    achieves = serializers.CharField(max_length=200)

class RatingSerializer(serializers.Serializer):
    user_id_rated = serializers.IntegerField()
    session_rating = serializers.DateField()

class DetailRatingSerializer(serializers.Serializer):
    user_id_accessor = serializers.IntegerField()
    rating_id = serializers.IntegerField()
    description = serializers.CharField()
    score = serializers.IntegerField()
class LogRatingSerializer(serializers.Serializer):
    detail_rating_id = serializers.IntegerField()
    update_at = serializers.DateTimeField()
