from rest_framework import serializers
from ..serializers import BasicSerializer
from ..role.serializers import RoleSerializer
from ..permission.serializers import PermissionSerializer

class RolePermissionSerializer(BasicSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    role_id = RoleSerializer(source="role_set", many = True)
    permission_id = PermissionSerializer(source = "permission_set", many = True)