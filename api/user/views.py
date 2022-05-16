from rest_framework.viewsets import ViewSet
from .serializers import UserSerializer
from core.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import orjson
from django.db.models import F
from rest_framework.viewsets import ModelViewSet



class UserViewSet(ModelViewSet):

    lookup_field = User.objects.all()

    serializer_class = UserSerializer


    
    def create(self, request, *args, **kwargs):
        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        data = orjson.loads(request.body)

        username = data.get("username", None)
        password = data.get("password", None)
        first_name = data.get("first_name", None)
        last_name = data.get("last_name", None)
        email = data.get("email", None)
        position_role = data.get("position_role", None)
        rank = data.get("rank", None)

        user = User.objects.create(
            username = username,
            password = make_password(password),
            first_name = first_name,
            last_name = last_name,
            email = email,
            position_role = position_role,
            rank = rank,
        )
        user.save()

        if not user:
            return Response("Errol", status=status.HTTP_400_BAD_REQUEST)
        return Response("Successful", status=status.HTTP_201_CREATED)