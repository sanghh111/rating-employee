from rest_framework.viewsets import ViewSet
from core.project.models import Project
from ..serializers import ProjectSerializer
from rest_framework.response import Response
from rest_framework import status
import orjson
from django.db.models import F
from api.base.api_view import BaseAPIView

# from api.base.decorator import permission, has_permission

class ProjectViewSet(BaseAPIView):

    queryset = Project.objects.all()

    def list(self, request):
        # permission
        request.user.verify_permission('view_project')

        project_id = self.request.query_params.get('id', None)
        project_name = self.request.query_params.get('project_name', None)
        description = self.request.query_params.get('description', None)
        tech_stack = self.request.query_params.get('tech_stack', None)

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
  
    def create(self, request, *args, **kwargs):
        # permission
        request.user.verify_permission('add_project')
        
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
        if not project:
            return Response("Errol", status=status.HTTP_400_BAD_REQUEST)
        return Response("Create successful", status=status.HTTP_201_CREATED)
