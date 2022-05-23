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
