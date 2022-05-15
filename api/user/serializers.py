from rest_framework import serializers
from ..serializers import BasicSerializer

class UserSerializer(BasicSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    position = serializers.CharField(required=False)
    rank = serializers.CharField(required=False)

    def validate_confirm_password(self):
        pass

# ([a-z0-9]+)@minerva[.]com
    def validated_email(self, valuedata):
        
        return 