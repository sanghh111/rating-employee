from core.models import UserRole, User, Role
from rest_framework.response import Response
from rest_framework import status
import orjson
from django.db.models import F
from api.base.api_view import BaseAPIView
from django.forms.models import model_to_dict
from django.http import Http404
from drf_yasg import openapi 
from drf_yasg.utils import swagger_auto_schema


class UserRoleViewSet(BaseAPIView):

    queryset = UserRole.objects.all()

    @swagger_auto_schema(
        operation_description= "LIST USER ROLE",
        responses={
            200 : "OK",
            401: "UNAUTHORIZED"
        })
    def list(self, request):
        # permission

        user_role = UserRole.objects.annotate(
            user_name = F('user_id__username'),
            role_name = F('role_id__name'),
            priority = F('role_id__priority'),
        ).values(
            'id',
            'user_id',
            'user_name',
            'role_id',
            'role_name',
            'priority',
        )
        return Response(user_role)


    @swagger_auto_schema(
        operation_description= "CREATE USER ROLE",
        request_body= openapi.Schema(
            type= openapi.TYPE_OBJECT,
            properties={
                'user_id' : openapi.Schema(type= openapi.TYPE_INTEGER),
                'role_id' : openapi.Schema(type= openapi.TYPE_INTEGER),
            }
        ),
        responses={
            201 : "CREATE OK",
            400 : "MISSING DATA",
            401 : "UNAUTHORIZED",
            404 : "NOT FOUND"
        }
    )
    def create(self, request):
        # permission

        data = request.data

        user_id = data.get('user_id', None)
        role_id = data.get('role_id', None)

        user = User.objects.filter(pk = user_id).first()
        role = Role.objects.filter(pk = role_id).first()

        user_role = UserRole.objects.create(
            user_id = user,
            role_id = role,
        )
        if not user_role:
            return Response("Errol", status=status.HTTP_400_BAD_REQUEST)
        return Response("Create successful", status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_description= "UPDATE USER ROLE",
        request_body= openapi.Schema(
            type= openapi.TYPE_OBJECT,
            properties={
                'id' : openapi.Schema(type= openapi.TYPE_INTEGER),
                'user_id' : openapi.Schema(type= openapi.TYPE_INTEGER),
                'role_id' : openapi.Schema(type= openapi.TYPE_INTEGER),
            }
        ),
        responses={
            200 : "UPDATE OK",
            400 : "MISSING DATA",
            401 : "UNAUTHORIZED",
            404 : "NOT FOUND"
        }
    )
    def update(self, request):
        # permission

        data = request.data

        id = data.get('id', None)
        user_id = data.get('user_id', None)
        role_id = data.get('role_id', None)

        user_role = UserRole.objects.filter(pk=id).first()
        if not user_role:
            return Response("User role not found", status=status.HTTP_404_NOT_FOUND)

        user = User.objects.filter(pk=user_id).first()
        role = Role.objects.filter(pk=role_id).first()

        if user:
            user_role.user_id = user
        if role:
            user_role.role_id = role

        data = model_to_dict(user_role)
        return Response(data)


    @swagger_auto_schema(
        operation_description= "DELETE USER ROLE",
        request_body= openapi.Schema(
            type= openapi.TYPE_OBJECT,
            properties={
                'id' : openapi.Schema(type= openapi.TYPE_INTEGER),
            }
        ),
        responses={
            200 : "DELETE OK",
            400 : "MISSING DATA",
            401 : "UNAUTHORIZED",
            404 : "NOT FOUND"
        }
    )
    def delete(self, request):
        # permission

        data = request.data

        id = data.get('id', None)

        user_role = UserRole.objects.filter(pk=id).first()
        if not user_role:
            return Response("User role not found", status=status.HTTP_404_NOT_FOUND)

        try:
            user_role.delete()
            return Response("Deleted", status=status.HTTP_200_OK)
        except:
            return Response("Delete unsuccessful", status=status.HTTP_400_BAD_REQUEST)

