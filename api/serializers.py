from rest_framework import serializers
from models import User, Skill, UserSkill, GroupSkill, ProjectUserWork, Project, Rating, LogRating, DetailRating

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, required=False)
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    position = serializers.CharField(required=False)
    rank = serializers.CharField(required=False)
#
# class LoginSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)

class SkillSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, required=False)
    skill_name = serializers.CharField()
    group_skill_id = serializers.GroupSkillSerializer()

class GroupSkillSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, required=False)
    group_skill_name = serializers.CharField()

class UserSkillSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, required=False)
    skill_id = serializers.SkillSerializer()
    user_id = serializers.UserSerializer()
    year_of_experience = serializers.IntegerField()
    level = serializers.CharField()

class ProjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, required=False)
    project_name = serializers.CharField()
    description = serializers.CharField()
    date_start = serializers.DateField()
    date_end = serializers.DateField()
    tech_stack = serializers.CharField()

class ProjectUserWorkSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, required=False)
    project_id = serializers.ProjectSerializer()
    user_id = serializers.UserSerializer()
    position = serializers.CharField()
    work = serializers.CharField()
    achieves = serializers.CharField()

class RatingSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, required=False)
    user_id_rated = serializers.UserSerializer()
    session_rating = serializers.DateField()

class DetailRatingSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, required=False)
    user_id_accessor = serializers.UserSerializer()
    rating_id = serializers.RatingSerializer()
    description = serializers.CharField()
    score = serializers.IntegerField()

class LogRatingSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, required=False)
    detail_rating_id = serializers.DetailRatingSerializer(read_only=True, required=False)
    update_at = serializers.DateTimeField()
