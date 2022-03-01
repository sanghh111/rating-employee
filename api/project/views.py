from rest_framework.viewsets import ViewSet
from app.project.models import Project
from .serializers import ProjectSerializer

from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import orjson
from django.db.models import F


class ProjectViewSet(ViewSet):
    def list(self, request):

        project_name = self.request.query_params.get('project_name', None)
        description = self.request.query_params.get('description', None)
        tech_stack = self.request.query_params.get('tech_stack', None)

        projects = Project.objects.all()

        if project_name:
            projects = projects.filter(project_name__contains = project_name)
        if description:
            projects = projects.filter(description__contains = description)
        if tech_stack:
            projects = projects.filter(tech_stack__contains = tech_stack)

        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
  
    def create(self, request, *args, **kwargs):
        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        data = orjson.loads(request.body)
        
        project_name = data.get('project_name', None)
        description = data.get('description')
        date_start = data.get('date_start')
        date_end = data.get('date_end')
        tech_stack = data.get('tech_stack')

        project = Project.objects.create(
            project_name = project_name,
            description = description,
            date_start = date_start,
            date_end = date_end,
            tech_stack = tech_stack
            )
        if project:
            return Response("Create successful", status=status.HTTP_201_CREATED)
        else:
            return Response("Errol", status=status.HTTP_400_BAD_REQUEST)

class ProjectDetailViewSet(ViewSet):
    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get_detail(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def update(self, request, pk, format = None):
        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        else:
            data = orjson.loads(request.body)

        project_name = data.get('project_name', None)
        description = data.get('description', None)
        date_start = data.get('date_start', None)
        date_end = data.get('date_end', None)
        tech_stack = data.get('tech_stack', None)    

        project = Project.objects.filter(pk = pk).first()


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

        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        project = self.get_object(pk)
        try:
            project.delete()
            return Response("Deleted", status=status.HTTP_200_OK)
        except: 
            return Response("Delete unsuccessful", status=status.HTTP_400_BAD_REQUEST)

