from rest_framework.viewsets import ViewSet
from core.models import Project, ProjectUserWork, User
from .serializers import ProjectUserWorkSerializer

from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import orjson
from django.db.models import F
from api.base.api_view import BaseAPIView



class ProjectUserWorkViewSet(BaseAPIView):

    queryset  = ProjectUserWork.objects.all()

    def list(self, request):
        # permission

        project_user_works = ProjectUserWork.objects.annotate(
            username=F('user_id__username'),
            user_rank=F('user_id__rank'),
            project_name=F('project_id__project_name'),
            project_tech_stack=F('project_id__tech_stack'),
        ).values(
            'id',
            'user_id',
            'username',
            'user_rank',
            'project_name',
            'position',
            'work',
            'project_tech_stack',
            'achieves'
        )
        return Response(project_user_works)

    def create(self, request, *args, **kwargs):
        # permission
        

        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        data = orjson.loads(request.body)

        project_id = data.get('project_id', None)
        user_id = data.get('user_id', None)
        position = data.get('position', None)
        work = data.get('work', None)
        achieves = data.get('achieves', None)

        project = Project.objects.filter(pk=project_id).fisrt()
        user = User.objects.filter(pk=user_id).fisrt()

        project_user_work = ProjectUserWork.objects.create(
            project_id = project,
            user_id = user,
            position = position,
            work = work,
            achieves = achieves
        )

        if not project_user_work:
            return Response("Errol", status=status.HTTP_400_BAD_REQUEST)
        return Response("Create successful", status=status.HTTP_201_CREATED)

