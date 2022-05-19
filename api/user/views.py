from datetime import datetime
from venv import create
from django.db import DataError
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
from ..base.permissions import IsActiveUser
from rest_framework.permissions import IsAuthenticated

class UserViewSet(ModelViewSet):

    queryset =  User.objects.all()


    serializer_class = UserSerializer

    #override get_permission
    def get_permissions(self):
        if self.action == 'list' and self.action == 'update':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsActiveUser]
        return [permission() for permission in permission_classes]

    #config method create
    def create(self, request, *args, **kwargs):
        if request.body:
            
            data   = orjson.loads(request.body)

            data['password'] = make_password(data['password'])
            data.update(
                create_at = datetime.now(),
                create_by = request.user.id
            )
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response('No data',status= status.HTTP_400_BAD_REQUEST)

    #Update Profile User
    def update(self, request, *args, **kwargs):
        if  request.body :
            data = orjson.loads(request.body)
            try: 
                if data['password']:
                    return Response(
                        data = {
                            'error' : 'deny change password',
                        },
                        status = status.HTTP_500_INTERNAL_SERVER_ERROR
                    )
                if data['rank']:
                    if request.user.rank == "MANAGER":
                        return Response(
                        data = {
                            'error' : 'deny change rank',
                        },
                        status = status.HTTP_500_INTERNAL_SERVER_ERROR
                    )
            except KeyError:
                data.update(
                    modified_by = request.user.id,
                    modified_at = datetime.now()
                )
                partial = kwargs.pop('partial', False)
                instance = self.get_object()
                serializer = self.get_serializer(instance, data=data, partial=partial)
                self.perform_update(serializer)

                if getattr(instance, '_prefetched_objects_cache', None):
                    # If 'prefetch_related' has been applied to a queryset, we need to
                    # forcibly invalidate the prefetch cache on the instance.
                    instance._prefetched_objects_cache = {}

                return Response(serializer.data)
        else:
            return Response('No data',status= status.HTTP_400_BAD_REQUEST)





    def find_user(self,request,*args, **kwargs):
        """
        action to int : exact, iexact, gt , gte, lt,lte
        action to string : exact,iexact, startwith, endwith, istartwith, iendwith
        action to list : contains,icontains
        aciton to annotate : annotate 
        action 'exact, iexact, contains, icontains, gt, gte, lt, lte'
        
        {
            [{
                'name' : {
                    'atribue' : 'a'
                    'action': exact
                } 
            },

        }
        """


        pass

    def delete_user(self,request,*args,**kwargs):
        if request.body:
            data = orjson.loads(request.body)
            try:
                user = User.objects.get(**data)
                user.delete()
                return Response(
                    data = {
                        'message' :  'delete success'
                    },
                    status= status.HTTP_200_OK
                )
            except User.DoesNotExist:
                return Response('Not found', status=status.HTTP_404_NOT_FOUND)  
        else : 
            return Response('no_data',status= status.HTTP_400_BAD_REQUEST)
