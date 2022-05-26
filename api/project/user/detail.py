from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from ..serializers import ProjectSerializer
from core.project.models import Project
from rest_framework.response import Response 
from django.db import  models
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class APIProjectDetail(ViewSet):
    
    permission_classes = [IsAuthenticated]

    #find theo keyword
    @swagger_auto_schema(
        operation_description= "LIST PROJECT BY USER",
        manual_parameters= [openapi.Parameter('id',openapi.IN_QUERY,type= openapi.TYPE_INTEGER)],
        responses= {
            '200':'OK'
        })
    def list(self, request, *args, **kwargs):
        

        id = self.request.query_params.get('id',None)
    
        project = Project.objects.annotate(user = models.F('project_id__user_id')).filter(user =request.user.id).order_by('id')
    
        if id :
            project = project.filter(id = id)

        data = ProjectSerializer(project, many = True).data

        return Response(data,200)

