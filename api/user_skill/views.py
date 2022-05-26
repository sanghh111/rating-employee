from rest_framework.viewsets import ViewSet
from .serializers import UserSkillSerializer
from core.models import UserSkill, Skill, User

from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import orjson
from django.db.models import F
from api.base.api_view import BaseAPIView
from drf_yasg import openapi 
from drf_yasg.utils import swagger_auto_schema


class UserSkillViewSet(BaseAPIView):

    queryset = UserSkill.objects.all()

    @swagger_auto_schema(
        operation_description="LIST UserSkill",
        manual_parameters= [
            openapi.Parameter('skill_id',openapi.IN_QUERY,type= openapi.TYPE_INTEGER),
            openapi.Parameter('user_id',openapi.IN_QUERY,type= openapi.TYPE_INTEGER),
            openapi.Parameter('year_of_experience',openapi.IN_QUERY,type= openapi.TYPE_INTEGER),
            openapi.Parameter('level',openapi.IN_QUERY,type= openapi.TYPE_INTEGER),
        ],
        responses= {
            200: "OK"
        }
    )
    def list(self, request):
        # permission



        skill_id =request.query_params.get('skill_id', None)
        user_id = request.query_params.get('user_id', None)
        year_of_experience =request.query_params.get('year_of_experience', None)
        level =request.query_params.get('level', None)

        user_skills = UserSkill.objects.annotate(
            user_skill_id = F('id'),
            skill_name = F('skill_id__name'),
            username = F('user_id__username'),
        ).values(
            'user_skill_id',
            'skill_id',
            'skill_name',
            'user_id',
            'username',
            'year_of_experience',
            'level'
        )

        if skill_id:
            user_skills = user_skills.filter(skill_id=skill_id)
        if user_id:
            user_skills = user_skills.filter(user_id=user_id)
        if year_of_experience:
            user_skills = user_skills.filter(year_of_experience=year_of_experience)
        if level:
            user_skills = user_skills.filter(level=level)
        
        return Response(user_skills)
    


    @swagger_auto_schema(
        operation_description="CREATE SKILL FOR USER",
        request_body= openapi.Schema(
            type= openapi.TYPE_OBJECT,
            properties={
                'skill_id': openapi.Schema(type= openapi.TYPE_INTEGER),
                'user_id': openapi.Schema(type= openapi.TYPE_INTEGER),
                'year_of_experience': openapi.Schema(type= openapi.TYPE_INTEGER),
                'level': openapi.Schema(type= openapi.TYPE_INTEGER),
            }
        ),
        responses=
        {
            201:"CREATE OK",
            400:"ERROR",
            401: "UNAUTHORIZED",
            404:"NOT FOUND"

        }
        # responses=
    )
    def create(self, request, *args, **kwargs):
        # permission
        

        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        data = orjson.loads(request.body)

        skill_id = data.get("skill_id", None)
        user_id = data.get("user_id", None)
        year_of_experience = data.get("year_of_experience", None)
        level = data.get("level", None)

        skill = Skill.objects.filter(pk = skill_id).first()
        user = User.objects.filter(pk = user_id).first()

        user_skill = UserSkill.objects.create(
            skill_id = skill,
            user_id = user,
            year_of_experience = year_of_experience,
            level = level
        )

        if not user_skill:
            return Response("Errol", status=status.HTTP_400_BAD_REQUEST)
        return Response("Create successful", status=status.HTTP_201_CREATED)

