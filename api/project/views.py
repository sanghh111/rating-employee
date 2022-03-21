from rest_framework.viewsets import ViewSet
from app.project.models import Project
from .serializers import ProjectSerializer
from rest_framework.response import Response
from rest_framework import status
import orjson
from django.db.models import F
# from rest_framework.permissions import IsAuthenticated
# from api.base.authentication import TokenAuthentication
from api.base.api_view import BaseAPIView

# from api.base.decorator import permission, has_permission

class ProjectViewSet(BaseAPIView):

    def list(self, request):
        # #permission
        user = self.user
        if user.verify_permission('view_project') == False:
            return Response("User not permission", status=status.HTTP_407_PROXY_AUTHENTICATION_REQUIRED)


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
        #permission
        user = self.user
        if user.verify_permission('add_project') == False:
            return Response("User not permission", status=status.HTTP_407_PROXY_AUTHENTICATION_REQUIRED)
        
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


