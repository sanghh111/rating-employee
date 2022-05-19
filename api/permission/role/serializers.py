from rest_framework import serializers
from ..serializers import BasicSerializer
from api.role.serializers import RoleSerializer
from ..serializers import PermissionSerializer

class RolePermissionSerializer(BasicSerializer):
    role_id = RoleSerializer( many = True)
    permission_id = PermissionSerializer( many = True)