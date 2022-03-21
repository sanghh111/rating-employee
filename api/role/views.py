from .serializers import RoleSerializer
from app.models import Role

from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import orjson
from django.db.models import F
from api.base.api_view import BaseAPIView

class RoleViewSet(BaseAPIView):
    def list(self, request):
        # # #permission
        # user = self.user
        # if user.verify_permission('view_role') == False:
        #     return Response("Authentication required", status=status.HTTP_407_PROXY_AUTHENTICATION_REQUIRED)

        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        #permission
        user = self.user
        if user.verify_permission('add_role') == False:
            return Response("Authentication required", status=status.HTTP_407_PROXY_AUTHENTICATION_REQUIRED)

        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        data = orjson.loads(request.body)

        name = data.get('name', None)
        description = data.get('description', None)

        role = Role.objects.create(
            name=name,
            description=description
        )

        if not role:
            return Response("Errol", status=status.HTTP_400_BAD_REQUEST)
        return Response("Create successful", status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        #permission
        # user = self.user
        # if user.verify_permission('delete_role') == False:
        #     return Response("Authentication required", status=status.HTTP_407_PROXY_AUTHENTICATION_REQUIRED)

        role = Role.objects.get(pk=pk)
        if role:
            try:
                role.delete()
                return Response("Deleted", status=status.HTTP_200_OK)
            except:
                return Response("Delete unsuccessful", status=status.HTTP_400_BAD_REQUEST)
        return Response("Role not found", status=status.HTTP_404_NOT_FOUND)