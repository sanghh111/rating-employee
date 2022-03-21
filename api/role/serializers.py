from rest_framework import serializers
from ..serializers import BasicSerializer

class RoleSerializer(BasicSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=100)

