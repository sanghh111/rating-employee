from rest_framework import serializers
from ..serializers import BasicSerializer

class UserSerializer(BasicSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    position = serializers.CharField(required=False)
    rank = serializers.CharField(required=False)