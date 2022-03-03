from rest_framework.viewsets import ViewSet
from .serializers import UserSerializer
from app.models import User

from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import orjson
from django.db.models import F

class UserViewSet(ViewSet):
    def list(self, request):
        users = User.objects.all().values()
        return Response(users)
    
    def create(self, request, *args, **kwargs):
        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        
        data = orjson.loads(request.body)
        
        
        user_name = data.get("user_name", None)
        password = data.get("password", None)
        first_name = data.get("first_name", None)
        last_name = data.get("last_name", None)
        email = data.get("email", None)
        position = data.get("position", None)
        rank = data.get("rank", None)

        user = User.objects.create(
            user_name = user_name,
            password = password,
            first_name = first_name,
            last_name = last_name,
            email = email,
            position = position,
            rank = rank,
        )

        if not user:
            return Response("Errol", status=status.HTTP_400_BAD_REQUEST)
        return Response("Successful", status=status.HTTP_201_CREATED)