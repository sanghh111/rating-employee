import re
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from ..serializers import ProjectSerializer
from core.project.models import Project
from rest_framework.response import Response 
from django.db import  models
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
class APIProject(ViewSet):
    
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description= "LIST PROJECT BY USER",
        responses= {
            '200':'OK'
        }
    )
    def list(self, request, *args, **kwargs):
        project = Project.objects.annotate(user = models.F('project_id__user_id')).filter(user =request.user.id).order_by('id')
    
        data = ProjectSerializer(project,many = True).data

        return Response(data,200)

