import imp
from ..base.api_view import BaseAPIView
from core.permission.models import Permission
from rest_framework.response import Response
from rest_framework import status
from .serializers import PermissionSerializer
class APIPermission(BaseAPIView):


    def list(self, request, *args, **kwargs):
        
        permission = Permission.objects.all()

        data = PermissionSerializer(permission,many=True).data

        return Response(data = data,
                        status= status.HTTP_200_OK)