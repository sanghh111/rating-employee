from .serializers import RoleSerializer
from core.models import Role

from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import orjson
from django.db.models import F
from api.base.api_view import BaseAPIView

class RoleViewSet(BaseAPIView):

    queryset = Role.objects.all()

    def list(self, request):
        # permission
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        # permission
        request.user.verify_permission('add_role')

        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        data = orjson.loads(request.body)

        name = data.get('name', None)
        description = data.get('description', None)
        priority = data.get('priority', None)
        role = Role.objects.create(
            name=name,
            description=description,
            priority = priority,
        )

        if not role:
            return Response("Errol", status=status.HTTP_400_BAD_REQUEST)
        return Response("Create successful", status=status.HTTP_201_CREATED)

    def delete(self, request):
        # permission

        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        data = orjson.loads(request.body)

        role_id = data.get("role_id", None)
        role = Role.objects.filter(pk=role_id).first()

        if role:
            try:
                role.delete()
                return Response("Deleted", status=status.HTTP_200_OK)
            except:
                return Response("Delete unsuccessful", status=status.HTTP_400_BAD_REQUEST)
        return Response("Role not found", status=status.HTTP_404_NOT_FOUND)