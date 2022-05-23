from rest_framework.viewsets import ViewSet
from core.project.models import Project
from ..serializers import ProjectSerializer

from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import orjson
from django.db.models import F
from api.base.api_view import BaseAPIView
from core.user.models import User
class ProjectDetailViewSet(BaseAPIView):

    queryset = Project.objects.all()

    def update(self, request, format = None):

        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        else:
            data = orjson.loads(request.body)

        id = data.get('id', None)
        project_name = data.get('project_name', None)
        description = data.get('description', None)
        date_start = data.get('date_start', None)
        date_end = data.get('date_end', None)
        tech_stack = data.get('tech_stack', None)    
        project_manager = data.get('project_manager',None)
        project = Project.objects.filter(pk=id).first()
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

        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    
    def delete(self, request):
        # permission
        request.user.verify_permission('delete_project')

        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        data = orjson.loads(request.body)

        id = data.get('project_id', None)

        project = Project.objects.filter(pk=id).first()
        if not project:
            return Response("Project not found", status=status.HTTP_404_NOT_FOUND)
        try:
            project.delete()
            return Response("Deleted", status=status.HTTP_200_OK)
        except: 
            return Response("Delete unsuccessful", status=status.HTTP_400_BAD_REQUEST)
