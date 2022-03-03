from rest_framework.viewsets import ViewSet
from app.models import Project, ProjectUserWork, User
from .serializers import ProjectUserWorkSerializer

from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import orjson
from django.db.models import F

class ProjecUserWorkDetailViewSet(ViewSet):
    def update(self, request, pk):
        project_user_work = ProjectUserWork.objects.get(pk = pk)
        if not project_user_work:
            return Response("not found", status=status.HTTP_404_NOT_FOUND)

        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        data = orjson.loads(request.body)
        
        project_id = data.get('project_id', None)
        user_id = data.get('user_id', None)
        position = data.get('position', None)
        work = data.get('work', None)
        achieves = data.get('achieves', None)
        
        project = Project.objects.get(pk = project_id)
        user = User.objects.get(pk = user_id)

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

    def delete(self, request, pk):
        project_user_work = ProjectUserWork.objects.get(pk = pk)
        if not project_user_work:
            return Response("not found", status=status.HTTP_404_NOT_FOUND)
        
        try:
            project_user_work.delete()
            return Response("Delete successful", status=status.HTTP_200_OK)
        except:
            return Response("Delete unsuccessful", status=status.HTTP_400_BAD_REQUEST)