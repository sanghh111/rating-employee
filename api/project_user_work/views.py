from rest_framework.viewsets import ViewSet
from core.models import Project, ProjectUserWork, User
from .serializers import ProjectUserWorkSerializer

from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import orjson
from django.db.models import F
from api.base.api_view import BaseAPIView
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class ProjectUserWorkViewSet(BaseAPIView):

    queryset  = ProjectUserWork.objects.all()
    
    @swagger_auto_schema(
        operation_description= "LIST PROJECT USER WORK",
        responses= {
            '201':"OK"
        }
        )
    def list(self, request, *args, **kwargs):
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

    @swagger_auto_schema(
        operation_description= "CREATE PROJECT USER WORK",
        request_body= openapi.Schema(
            type =  openapi.TYPE_OBJECT,
            properties= {
                'project_id': openapi.Schema(type =  openapi.TYPE_STRING),
                'user_id': openapi.Schema(type =  openapi.TYPE_STRING),
                'position': openapi.Schema(type =  openapi.TYPE_STRING),
                'work': openapi.Schema(type =  openapi.TYPE_STRING),
                'achieves': openapi.Schema(type =  openapi.TYPE_STRING),
            }
        ),
        responses={
            201 :"CREATE OK",
            404 :"NOT FOUND"
        }
    )
    def create(self, request, *args, **kwargs):
        
        seriliazer = ProjectUserWorkSerializer(data = request.data)
        seriliazer.is_valid(raise_exception=True)
        data =seriliazer.data

        project_id = data.get('project_id', None)
        user_id = data.get('user_id', None)
        position = data.get('position', None)
        work = data.get('work', None)
        achieves = data.get('achieves', None)

        try:
            project = Project.objects.get(pk=project_id)
        except Project.DoesNotExist:
            return Response("NOT FOUND", 404)
        try:
            user = User.objects.get(pk=user_id)
        except:
            return Response("NOT FOUND",404)
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

