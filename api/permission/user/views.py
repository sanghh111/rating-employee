import imp
from rest_framework.response import Response
from api.base.api_view import CustomAPIView
from core.models import UserPermission, User, Permission
from .serializers import UserPermissionSerializer
import orjson
from api.base.permissions import IsActiveUser

class APIUserPermission(CustomAPIView):


    queryset =  UserPermission.objects.all()

    def create(self,request,*args, **kwargs):
        if request.body:
            data =  orjson.loads(request.body)

            user_id = data.get('user_id', None)

            permission_id = data.get('permission_id',None)

            if user_id :
                try:
                    user = User.objects.get(id = user_id)
                except User.DoesNotExist:
                    return Response(
                        data = "NOT Found USER",
                        status= 404
                    )
            else:
                return Response(
                        data = "NOT Found USER",
                        status= 404
                    )

            if permission_id:
                try:
                    permission = Permission.objects.get(id = permission_id)
                except Permission.DoesNotExist:
                    return Response(
                        data = "NOUT FOUND PERMISSION",
                        status= 404
                    )
            else:
                return Response(
                        data = "NOUT FOUND PERMISSION",
                        status= 404
                    )

            data = {
                'user' : user,
                'permission_id': permission,
            }       
            
            try: 
                UserPermission.objects.get(**data)
            except UserPermission.DoesNotExist:
                data.update(created_by = f'{request.user.first_name} {request.user.last_name}')
                UserPermission.objects.create(**data)

            serializer = UserPermissionSerializer(data)

            return Response(serializer.data , status= 201)
        else:
            return Response(data = "NO BODY DATA"
                            ,status= 400)   

    def delete(self, request, *args, **kwargs):
            if request.body:
                data =  orjson.loads(request.body)

            user_id = data.get('user_id', None)

            permission_id = data.get('permission_id',None)

            if user_id :
                try:
                    user = User.objects.get(id = user_id)
                except User.DoesNotExist:
                    return Response(
                        data = "NOT Found USER",
                        status= 404
                    )
            else:
                return Response(
                        data = "NOT Found USER",
                        status= 404
                    )

            if permission_id:
                try:
                    permission = Permission.objects.get(id = permission_id)
                except Permission.DoesNotExist:
                    return Response(
                        data = "NOUT FOUND PERMISSION",
                        status= 404
                    )
            else:
                return Response(
                        data = "NOUT FOUND PERMISSION",
                        status= 404
                    )
            try: 
                instace = UserPermission.objects.get(**data)
                instace.delete()
                return Response(data= "DELETE OK" , status=200)
            except UserPermission.DoesNotExist:
                return Response( 
                        data= "NOT FOUND USERPERMISSION",
                        status = 404
                        )

                    