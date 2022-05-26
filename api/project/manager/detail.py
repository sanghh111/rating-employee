from rest_framework.viewsets import ViewSet
from core.project.models import Project
from ..serializers import ProjectRequsetSerializer, ProjectSerializer

from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import orjson
from django.db.models import F
from api.base.api_view import BaseAPIView
from core.user.models import User
from drf_yasg import openapi 
from drf_yasg.utils import swagger_auto_schema
class ProjectDetailViewSet(BaseAPIView):

    queryset = Project.objects.all()

    @swagger_auto_schema(operation_description="UPDATE PROJECT",
                        request_body=openapi.Schema(
                            type= openapi.TYPE_OBJECT,
                            properties= {
                                'project_name':openapi.Schema(type = openapi.TYPE_STRING),
                                'description':openapi.Schema(type = openapi.TYPE_STRING),
                                'date_start':openapi.Schema(type = openapi.TYPE_STRING),
                                'date_end':openapi.Schema(type = openapi.TYPE_STRING),
                                'tech_stack':openapi.Schema(type = openapi.TYPE_STRING),
                                'project_manager':openapi.Schema(type = openapi.TYPE_STRING),
                            }
                        ),responses={
                            200 : 'UPDATE OK',
                            404 : "NOT FOUND PROJECT / USER"
                        }
            )
    def update(self, request, *args, **kwargs):

        serializer = ProjectRequsetSerializer(data = request.data)
        serializer.is_valid(True)
        data = serializer.data

        id = data.get('id', None)
        project_name = data.get('project_name', None)
        description = data.get('description', None)
        date_start = data.get('date_start', None)
        date_end = data.get('date_end', None)
        tech_stack = data.get('tech_stack', None)    
        project_manager = data.get('project_manager',None)
        project = Project.objects.filter(**kwargs).first()
        if not project:
            return Response("Project not found", status=status.HTTP_404_NOT_FOUND)

        if project_name:
            project.project_name = project_name
        if description:
            project.description = description
        if date_start:
            project.date_start = date_start
        if date_end:
            project.date_end = date_end
        if tech_stack:
            project.tech_stack = tech_stack
        if project_manager:
            try:
                project.project_manager =  User.objects.get(id = project_manager)
            except Project.DoesNotExist:
                return ("NOT FOUND",404)
        project.save()
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description= "DELETE PROJECT",
                        responses={
                            200 : "DELETE OK",
                            '404' : 'NOT FOUND PROJECT '
                        }
                        )
    def delete(self, request,*args, **kwargs):
        # permission

        project = Project.objects.filter(**kwargs).first()
        if not project:
            return Response("Project not found", status=status.HTTP_404_NOT_FOUND)
        try:
            project.delete()
            return Response("Deleted", status=status.HTTP_200_OK)
        except: 
            return Response("Delete unsuccessful", status=status.HTTP_400_BAD_REQUEST)
