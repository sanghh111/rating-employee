# from django.conf import settings
from rest_framework_simplejwt import views as JWTviews
from rest_framework.viewsets import ViewSet
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from api.base.authentication import BasicAuthentication
from rating_employee import settings
from django.contrib.auth import authenticate

class UserLoginViewSet(ViewSet):    
    
    authentication_classes = (BasicAuthentication,)
    permission_classes = ()

    def post(self, request):
        user = request.user
        context = {}
        context.update({
            'user_id': user.id,
            'token': user.get_key,
            'username': user.username,
        })
        return Response(context)