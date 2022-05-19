from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from ..serializers import ProjectSerializer
from core.project.models import Project
from rest_framework.response import Response 
from django.db import  models

class APIProject(ViewSet):
    
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        project = Project.objects.annotate(user = models.F('project_id__user_id')).filter(user =request.user.id).order_by('id')
    
        data = ProjectSerializer(project).data

        return Response(data,200)

    def retrive(self,request,*args, **kwargs):
        pass