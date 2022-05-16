from datetime import datetime
from venv import create
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
from ..base.permissions import IsManagerUser
from rest_framework.permissions import IsAuthenticated

class UserViewSet(ModelViewSet):


    lookup_field = User.objects.all()

    serializer_class = UserSerializer

    #override get_permission
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsManagerUser]
        return [permission() for permission in permission_classes]

    #config method create
    def create(self, request, *args, **kwargs):
        if not request.body:
            
            data   = orjson.loads(request.body)

            data['password'] = make_password(data['password'])
            data.update(
                create_at = datetime.now(),
                create_by = request.user.id
            )
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)


            return Response(serializer.data, status=status.HTTP_201_CREATED)

    
