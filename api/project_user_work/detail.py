import imp
from rest_framework.viewsets import ViewSet
from core.models import Project, ProjectUserWork, User
from .serializers import ProjectUserWorkSerializer

from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import orjson
from django.db.models import F
from api.base.api_view import BaseAPIView
from drf_yasg import openapi 
from drf_yasg.utils import  swagger_auto_schema

class ProjecUserWorkDetailViewSet(BaseAPIView):

    queryset = ProjectUserWork.objects.all()

    @swagger_auto_schema(
        operation_description= "UPDATE PROJECT USER WORK",
        request_body= openapi.Schema(
            type = openapi.TYPE_OBJECT,
            properties= {
                'id' : openapi.Schema(openapi.TYPE_STRING),
                'project_id' : openapi.Schema(openapi.TYPE_STRING),
                'user_id' : openapi.Schema(openapi.TYPE_STRING),
                'position' : openapi.Schema(openapi.TYPE_STRING),
                'work' : openapi.Schema(openapi.TYPE_STRING),
                'achieves' : openapi.Schema(openapi.TYPE_STRING),
                
            }
        )
        responses= {
            200 : "UPDATE OK"
            404 : "NOT FOUND"
        }

    )
    def update(self, request):
        # permission

        serializer = ProjectUserWorkSerializer(data = request.data)
        serializer.is_valid(True)
        data = serializer.data



        id = data.get('id', None)
        project_id = data.get('project_id', None)
        user_id = data.get('user_id', None)
        position = data.get('position', None)
        work = data.get('work', None)
        achieves = data.get('achieves', None)

        project_user_work = ProjectUserWork.objects.filter(pk=id).first()

        if not project_user_work:
            return Response("not found", status=status.HTTP_404_NOT_FOUND)

        project = Project.objects.filter(pk=project_id).first()
        user = User.objects.filter(pk=user_id).first()

        if project:
            project_user_work.project_id = project
        if user:
            project_user_work.user_id = user
        if position:
            project_user_work.position = position
        if work:
            project_user_work.work = work
        if achieves:
            project_user_work.achieves = achieves
    
        serializer = ProjectUserWorkSerializer(project_user_work)
        return Response(serializer.data)


    @swagger_auto_schema(operation_description= "DELETE USER WORK",
                        request_body= openapi.Schema(
                            type = openapi.TYPE_OBJECT,
                            properties= {
                                'id' : openapi.Schema(type=openapi.TYPE_INTEGER)
                            }
                        ),
                        responses={
                            200 : "DELETE OK",
                            '404':  "NOT FOUND"
                        })
    def delete(self, request):
        # permission


        id = request.data.('id', None)
        project_user_work = ProjectUserWork.objects.filter(pk = id).first()
        if not project_user_work:
            return Response("not found", status=status.HTTP_404_NOT_FOUND)
        try:
            project_user_work.delete()
            return Response("Delete successful", status=status.HTTP_200_OK)
        except:
            return Response("Delete unsuccessful", status=status.HTTP_400_BAD_REQUEST)