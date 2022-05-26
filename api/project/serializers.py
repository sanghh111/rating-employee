from rest_framework import serializers
from ..serializers import BasicSerializer
from api.user.serializers import UserSerializer
class ProjectSerializer(BasicSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    project_name = serializers.CharField()
    description = serializers.CharField()
    date_start = serializers.DateField()
    date_end = serializers.DateField()
    tech_stack = serializers.CharField()
    project_manager = UserSerializer()

class ProjectRequsetSerializer(BasicSerializer):
    project_name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    date_start = serializers.DateField(required=False)
    date_end = serializers.DateField(required=False)
    tech_stack = serializers.CharField(required=False)
    project_manager = serializers.IntegerField(required=False)