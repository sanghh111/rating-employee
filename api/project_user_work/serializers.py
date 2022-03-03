from rest_framework import serializers
from ..serializers import BasicSerializer
from ..project.serializers import ProjectSerializer
from ..user.serializers import UserSerializer

class ProjectUserWorkSerializer(BasicSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    project_id = ProjectSerializer()
    user_id = UserSerializer()
    position = serializers.CharField()
    work = serializers.CharField()
    achieves = serializers.CharField()

