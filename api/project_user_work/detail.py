from rest_framework.viewsets import ViewSet
from core.models import Project, ProjectUserWork, User
from .serializers import ProjectUserWorkSerializer

from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import orjson
from django.db.models import F
from api.base.api_view import BaseAPIView

class ProjecUserWorkDetailViewSet(BaseAPIView):

    queryset = ProjectUserWork.objects.all()

    def update(self, request):
        # permission


        request.user.verify_permission('change_projectuserwork')

        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        data = orjson.loads(request.body)

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

    def delete(self, request):
        # permission

        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        data = orjson.loads(request.body)

        id = data.get('id', None)
        project_user_work = ProjectUserWork.objects.filter(pk = id).first()
        if not project_user_work:
            return Response("not found", status=status.HTTP_404_NOT_FOUND)
        try:
            project_user_work.delete()
            return Response("Delete successful", status=status.HTTP_200_OK)
        except:
            return Response("Delete unsuccessful", status=status.HTTP_400_BAD_REQUEST)