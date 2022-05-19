from pyexpat import model
from api.serializers import BasicSerializer
from rest_framework import serializers
from  api.user.serializers import UserSerializer
from ..serializers import PermissionSerializer

class UserPermissionSerializer(BasicSerializer):
    
    user = UserSerializer()

    permission_id = PermissionSerializer()
