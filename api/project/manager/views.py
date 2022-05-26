from rest_framework.viewsets import ViewSet
from core.project.models import Project
from ..serializers import ProjectRequsetSerializer, ProjectSerializer
from rest_framework.response import Response
from rest_framework import status
import orjson
from django.db.models import F
from api.base.api_view import BaseAPIView
from core.user.models import User
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# from api.base.decorator import permission, has_permission

class ProjectViewSet(BaseAPIView):

    queryset = Project.objects.all()
    @swagger_auto_schema(
        operation_description="LIST ALL PROJECT ",
        manual_parameters=[
            openapi.Parameter('id',openapi.IN_QUERY,type=openapi.TYPE_INTEGER),
            openapi.Parameter('project_name',openapi.IN_QUERY,type=openapi.TYPE_STRING),
            openapi.Parameter('description',openapi.IN_QUERY,type=openapi.TYPE_INTEGER),
            openapi.Parameter('tech_stack',openapi.IN_QUERY,type=openapi.TYPE_INTEGER),

        ],
        responses= {
            200 : 'OK',
            401 : "Unauthorized"
        })
    def list(self, request,*args, **kwargs):
        # permission

        project_id = request.query_params.get('id', None)
        project_name = request.query_params.get('project_name', None)
        description = request.query_params.get('description', None)
        tech_stack = request.query_params.get('tech_stack', None)
        
        projects = Project.objects.all()
        if project_id:
            projects = projects.filter(id=project_id)
        if project_name:
            projects = projects.filter(project_name__contains=project_name)
        if description:
            projects = projects.filter(description__contains=description)
        if tech_stack:
            projects = projects.filter(tech_stack__contains=tech_stack)

        serializer = ProjectSerializer(projects, many=True)

        return Response(serializer.data)
  
    @swagger_auto_schema(
        operation_description="Create Project",
        request_body= openapi.Schema(
                type= openapi.TYPE_OBJECT,
                properties= {
                    'project_name' : openapi.Schema(type=openapi.TYPE_STRING),
                    'description' : openapi.Schema(type=openapi.TYPE_STRING),
                    'date_start' : openapi.Schema(type=openapi.FORMAT_DATE,description="YYYY-MM-DD" ),
                    'date_end' : openapi.Schema(type=openapi.FORMAT_DATE,description="YYYY-MM-DD"),
                    'tech_stack' : openapi.Schema(type=openapi.TYPE_STRING),
                    'project_manager' : openapi.Schema(type = openapi.TYPE_INTEGER)
                }
            ),
        responses={
            '201' : 'CREATE OK',
            '400' : 'MISSING DATA',
            '404' : 'NOT FOUND USER'
        }
    )
    def create(self, request, *args, **kwargs):
        # permission
        
        serializer = ProjectRequsetSerializer(data = request.data)
        print('serializer: ', serializer)
        serializer.is_valid(raise_exception=True)
        serializer = serializer.data

        project_name = serializer.get('project_name', None)
        description = serializer.get('description')
        date_start = serializer.get('date_start')
        date_end = serializer.get('date_end')
        tech_stack = serializer.get('tech_stack')
        project_manager = serializer.get('project_manager',None)
        if not project_manager:
            return Response("MISSING DATA",400)
        else:
            try:
                project_manager = User.objects.get(id = project_manager)
            except Project.DoesNotExist:
                return Response("DATA NOT FOUND",404)
        project = Project.objects.create(
            project_name = project_name,
            description = description,
            date_start = date_start,
            date_end = date_end,
            tech_stack = tech_stack,
            project_manager = project_manager
            )
        if not project:
            return Response("Errol", status=status.HTTP_400_BAD_REQUEST)
        return Response("Create successful", status=status.HTTP_201_CREATED)
