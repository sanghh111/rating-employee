from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from ..serializers import ProjectSerializer
from core.project.models import Project
from rest_framework.response import Response 
from django.db import  models

class APIProjectDetail(ViewSet):
    
    permission_classes = [IsAuthenticated]

    #find theo keyword
    def list(self, request, *args, **kwargs):
        

        id = self.request.query_params.get('id',None)
    
        project = Project.objects.annotate(user = models.F('project_id__user_id')).filter(user =request.user.id).order_by('id')
    
        if id :
            project = project.filter(id = id)

        data = ProjectSerializer(project, many = True).data

        return Response(data,200)

