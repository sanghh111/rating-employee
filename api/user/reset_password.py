from api.base.api_view import BaseAPIView
from .serializers import UserSerializer
from core.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import orjson
from django.db.models import F

class UserDetailViewSet(BaseAPIView):
    
    queryset = User.objects.all()

    def reset_password(self, request, *args, **kwargs):
        #request.user.verify_permission("reset_password")
        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        data = orjson.loads(request.body)

        user_id = data.get('user_id', None)
        new_password = data.get('password', None)
        retype_password = data.get('retype_password', None)

        if new_password.strip() == '' or new_password is None:
            return Response("Password invalid", status=status.HTTP_400_BAD_REQUEST)

        if new_password == retype_password:
            user = User.objects.filter(id=user_id)
            if user:
                user.password = make_password(new_password)
                user.token = None
                user.save()
                return Response("Reset password successful")
            else:
                return Response("User not found", status=status.HTTP_404_NOT_FOUND)
        else:
            return Response("Password mismatch", status=status.HTTP_400_BAD_REQUEST)