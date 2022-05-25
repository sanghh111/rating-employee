from requests import request
from rest_framework.viewsets import ViewSet
from core.models import GroupSkill, Skill
from .serializers import GroupSkillSerializer, SkillSerializer,GroupSkillRequestSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import orjson
from django.db.models import F
from api.base.api_view import BaseAPIView
from api.base.permissions import IsActiveUser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class GroupSkillViewSet(BaseAPIView):

    queryset = GroupSkill.objects.all()
    @swagger_auto_schema(   manual_parameters = [
                    openapi.Parameter('id', openapi.IN_QUERY,description="ID Group Skill",type=openapi.TYPE_INTEGER),
                    openapi.Parameter('name',openapi.IN_QUERY,description="Group Skill name ",type= openapi.TYPE_STRING),
                    ],
        operation_description="List group skill",
        responses={
            200: "ok"
        }
        )
    def list(self, request):

        group_skill_id = self.request.query_params.get("id", None)
        group_skill_name = self.request.query_params.get("name", None)

        group_skills = GroupSkill.objects.all()

        if group_skill_id:
            group_skills = group_skills.filter(id=group_skill_id)
        if group_skill_name:
            group_skills = group_skills.filter(group_skill_name__contains=group_skill_name)

        serializer = GroupSkillSerializer(group_skills, many=True)
        return Response(serializer.data)


    @swagger_auto_schema(
        operation_description="Create group skill",
        request_body = openapi.Schema( 
            type= openapi.TYPE_OBJECT,
            properties = {
                'group_skill_name': openapi.Schema(description= 'Name Group skill',type= openapi.TYPE_STRING)
                
            },
            required=None,),
        responses={
            201:'Create sussess',
            400:'Data invalid',
            409:'Data Confict',
        },
        format = openapi.TYPE_OBJECT
    )
    def create(self, request, *args, **kwargs):
        # if not request.body:
        #     print('b')
        #     return Response("Data invalid", status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     print('c')
        #     data = orjson.loads(request.body)

        data = GroupSkillRequestSerializer(data = request.data)

        if data.is_valid(raise_exception=True):

            data = data.data
        else :
            return Response("Data invalid",400)
        group_skill_name = data['group_skill_name']
        # group_skill_name = data.get('group_skill_name', None)
        try:
            GroupSkill.objects.get(
                group_skill_name = group_skill_name
            )
            return Response( data ="Name group skill conflict",
                            status= status.HTTP_409_CONFLICT)
        except GroupSkill.DoesNotExist:
            try:
                group_skill = GroupSkill.objects.create(
                    group_skill_name = group_skill_name
                )
            except Exception as e:
                return Response(e,status= status.HTTP_400_BAD_REQUEST)
        if group_skill:
            return Response("Create successful", status=status.HTTP_201_CREATED)
        else:
            return Response("Errol", status=status.HTTP_400_BAD_REQUEST)

class SkillViewSet(BaseAPIView):

    queryset = Skill.objects.all()

    @swagger_auto_schema(operation_description="LIST SKILL FROM GROUP SKILL",
    responses={
        '200': "OK",
        '404': "NOT FOUND SKILL"
    })
    def list(self, request):

        skills = Skill.objects.annotate(
                skill_id = F('id'),
                skill_name = F('name'),
                group_skill_name = F('group_skill_id__group_skill_name'),
            ).values(
                'skill_id',
                'skill_name',
                'group_skill_name',
            )
        if not skills:
            return Response("Errol", status=status.HTTP_404_NOT_FOUND)
        return Response(skills)
        
    @swagger_auto_schema(
        operation_description="CREEATE SKILL FOR GROUP",
        request_body= openapi.Schema(
            type= openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(description="Name skill",type=openapi.TYPE_STRING),
                'group_skill_id': openapi.Schema(description="Group skill id",type=openapi.TYPE_INTEGER)
            },
        ),request = {
            '201' : 'CREATED',
            '400' : 'DATA INVALID',
            '404' : 'NOT FOUND GROUP SKILL'
        }
    )
    def create(self, request, *args, **kwargs):
        
        # if not request.body:
        #     return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        
        # data = orjson.loads(request.body)
        # name = data.get('name', None)
        data  = SkillSerializer(data =  request.data)
        print('data: ', data)
        try:
            if data.is_valid(raise_exception= True):
                data = data.data
            else :
                return Response("Data invalid",400)
        except Exception as e:
            print(e)
        group_skill_id = request.data['group_skill_id']

        try:
            group_skill = GroupSkill.objects.get(pk = group_skill_id)
        except GroupSkill.DoesNotExist:
            return Response("NOT FOUND",404)

        Skill.objects.create(
                name = data['name'],
                group_skill_id = group_skill
            )
        return Response("Create successful", status=status.HTTP_201_CREATED)     
