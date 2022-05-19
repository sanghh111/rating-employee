from .serializers import RolePermissionSerializer
from core.models import RolePermission, Role, Permission

from rest_framework.response import Response
from rest_framework import status

import orjson
from django.db.models import F
from api.base.api_view import BaseAPIView

from django.forms.models import model_to_dict
class RolePermissionViewSet(BaseAPIView):

    queryset = RolePermission.objects.all()

    def list (self, request, *args, **kwargs):
        # permission

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
            role_permissions = role_permissions.filter(role_id = role_id)
        if permission_id:
            role_permissions = role_permissions.filter(permission_id = permission_id)
        
        return Response(role_permissions,200)

    def create(self, request):
        # permission

        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        data = orjson.loads(request.body)

        role_id = data.get('role_id', None)
        permission_id = data.get('permission_id', None)

        role = Role.objects.filter(id=role_id).first()
        permission = Permission.objects.filter(id=permission_id).first()

        role_permission = RolePermission.objects.create(
            role_id = role,
            permission_id = permission,
        )

        if not role_permission:
            return Response("Errol", status=status.HTTP_400_BAD_REQUEST)
        return Response("Create successful", status=status.HTTP_201_CREATED)

    def update(self, request):
        # permission

        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        data = orjson.loads(request.body)

        id = data.get('id', None)
        role_id = data.get('role_id', None)
        permission_id = data.get('permission_id', None)

        role_permission = RolePermission.objects.filter(pk=id)
        if not role_permission:
            return Response("Role permission not found", status=status.HTTP_404_NOT_FOUND)

        role = Role.objects.filter(id=role_id).first()
        permission = Permission.objects.filter(id=permission_id).first()

        if role: 
            role_permission.role_id = role 
        if permission:
            role_permission.permission_id = permission

        data = model_to_dict(role_permission)
        return Response(data)

        
    def delete(self, request):
        # permission
        request.user.verify_permission('delete_rolepermission')

        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        data = orjson.loads(request.body)

        id = data.get('id', None)

        role_permission = RolePermission.objects.filter(pk=id)
        if role_permission:
            try:
                role_permission.delete()
                return Response("Deleted", status=status.HTTP_200_OK)
            except:
                return Response("Delete unsuccessful", status=status.HTTP_400_BAD_REQUEST)
        return Response("Role not found", status=status.HTTP_404_NOT_FOUND)