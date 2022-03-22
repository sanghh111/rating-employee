from .serializers import RolePermissionSerializer
from app.models import RolePermission, Role, Permission

from rest_framework.response import Response
from rest_framework import status

import orjson
from django.db.models import F
from api.base.api_view import BaseAPIView

class RolePermissionViewSet(BaseAPIView):
    def list (self, request):

        #get data
        role_id = self.request.query_params.get('role_id', None)
        permission_id = self.request.query_params.get('permission_id', None)

        role_permissions = RolePermission.objects.annotate(
            role_name = F('role_id__name'),
            role_priority = F('role_id__priority'),
            permission_codename = F('permission_id__codename'),
            permission_name = F('permission_id__name')
        ).values(
            'id',
            'role_id',
            'role_name',
            'role_priority',
            'permission_id',
            'permission_codename',
            'permission_name',
        )
        
        if role_id:
            role_permissions = role_permissions.filter(role_id == role_id)
        if permission_id:
            role_permissions = role_permissions.filter(permission_id == permission_id)
        
        return Response(role_permissions)

    def create(self, request):
        
        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        data = orjson.loads(request.body)

        role_id = data.get('role_id', None)
        permission_id = data.get('permission_id', None)

        role = Role.objects.get(id=role_id)
        permission = Permission.objects.get(id=permission_id)

        role_permission = RolePermission.objects.create(
            role_id = role,
            permission_id = permission,
        )

        if not role_permission:
            return Response("Errol", status=status.HTTP_400_BAD_REQUEST)
        return Response("Create successful", status=status.HTTP_201_CREATED)