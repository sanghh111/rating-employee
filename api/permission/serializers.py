from rest_framework import serializers
from ..serializers import BasicSerializer

class PermissionSerializer(BasicSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    content_type_id = serializers.IntegerField(read_only=True, required=False)
    codename = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
