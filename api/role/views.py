from .serializers import RoleSerializer
from core.models import Role

from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import orjson
from django.db.models import F
from api.base.api_view import BaseAPIView
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class RoleViewSet(BaseAPIView):

    queryset = Role.objects.all()

    @swagger_auto_schema(
        operation_description= "LIST ROLE",
        responses={
            200 : "OK"
        }        
    )
    def list(self, request):
        # permission
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)
    

    @swagger_auto_schema(
        operation_description= "CREATE ROLE",
        request_body= openapi.Schema(
            type = openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'description': openapi.Schema(type=openapi.TYPE_STRING),
                'priority': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        responses= {
            201 : "CREATE OK",
            401 : "UNAUTHORIZED"
        }

    )
    def create(self, request):
        # permission

        data = request.data

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

    @swagger_auto_schema(
        operation_description= "DELETE ROLE",
        request_body= openapi.Schema(
            type = openapi.TYPE_OBJECT,
            properties={
                'role_id': openapi.Schema(type=openapi.TYPE_INTEGER),
            }
        ),
        responses= {
            200 : "DELETE OK",
            401 : "UNAUTHORIZED",
            404 : "NOT FOUND"
        }
        )
    def delete(self, request):
        # permission
        data = request.data

        role_id = data.get("role_id", None)
        role = Role.objects.filter(pk=role_id).first()

        if role:
            try:
                role.delete()
                return Response("Deleted", status=status.HTTP_200_OK)
            except:
                return Response("Delete unsuccessful", status=status.HTTP_400_BAD_REQUEST)
        return Response("Role not found", status=status.HTTP_404_NOT_FOUND)