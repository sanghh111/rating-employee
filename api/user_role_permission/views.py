from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import orjson
from django.db.models import F
from api.base.api_view import BaseAPIView
from core.views.models import UserRolePermission

class UserRolePermissionViewSet(BaseAPIView):

    queryset = UserRolePermission()

    def list(self, request):
        permissions = UserRolePermission.objects.all().values('permission_codename')
        permissions = list(permissions)
        return Response(permissions)    