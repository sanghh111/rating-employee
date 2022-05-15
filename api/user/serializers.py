from dataclasses import fields
from rest_framework.serializers import ModelSerializer 
from ..serializers import BasicSerializer
from core.user.models import User

class UserSerializer(ModelSerializer):

    class Meta():
        model = User
        fields = "__all__" 


# class UserSerializer(BasicSerializer):
#     # id = serializers.IntegerField(read_only=True, required=False)
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)
#     first_name = serializers.CharField(required=False)
#     last_name = serializers.CharField(required=False)
#     email = serializers.EmailField(required=False)
#     position = serializers.CharField(required=False)
#     rank = serializers.CharField(required=False)


# # ([a-z0-9]+)@minerva[.]com
#     def validated_email(self, valuedata):
        
#         return 