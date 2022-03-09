from rest_framework.viewsets import ViewSet
from app.models import Project, ProjectUserWork, User
from .serializers import ProjectUserWorkSerializer

from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import orjson
from django.db.models import F
from rest_framework_simplejwt.authentication import JWTAuthentication
class ProjectUserWorkViewSet(ViewSet):
    
    authentication_classes = (JWTAuthentication, )

    def list(self, request):
        
        project_user_works = ProjectUserWork.objects.annotate(
            username = F('user_id__username'),
            user_rank = F('user_id__rank'),
            project_name = F('project_id__project_name'),
            project_tech_stack = F('project_id__tech_stack'),
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

