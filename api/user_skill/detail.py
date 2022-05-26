
from .serializers import UserSkillSerializer
from core.models import UserSkill, Skill, User

from rest_framework.response import Response
from rest_framework import status
import orjson
from django.db.models import F
from api.base.api_view import BaseAPIView
from core.views.models import UserRolePermission
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
class UserSkillDetailViewSet(BaseAPIView):

    queryset = UserSkill.objects.all()
    @swagger_auto_schema(
        operation_description="DETAIL USER SKILL",
        request_body= openapi.Schema(
            type= openapi.TYPE_OBJECT,
            properties={
                'id':openapi.Schema(type = openapi.TYPE_INTEGER),
                'user_id':openapi.Schema(type = openapi.TYPE_INTEGER),
                'year_of_experience':openapi.Schema(type = openapi.TYPE_INTEGER),
                'level':openapi.Schema(type = openapi.TYPE_INTEGER),
            }
        ),
        responses={
            200 : "OK",
            401 : "UNAUTHORIZED",
            404 : "NOT FOUND"
        }
    )
    def update(self, request):
        # permission
        
        data = request.data

        id = data.get('id', None)
        skill_id = data.get("skill_id", None)
        user_id = data.get("user_id", None)
        year_of_experience = data.get("year_of_experience", None)
        level = data.get("level", None)

        user_skill = UserSkill.objects.filter(pk = id).first()
        if not user_skill:
            return Response("User skill not found", status=status.HTTP_404_NOT_FOUND)

        skill = Skill.objects.filter(pk = skill_id).first()
        user = User.objects.filter(pk = user_id).first()

        if skill_id:
            user_skill.skill_id = skill
        if user_id:
            user_skill.user_id = user
        if year_of_experience:
            user_skill.year_of_experience = year_of_experience
        if level:
            user_skill.level = level

        serializer = UserSkillSerializer(user_skill)
        return Response(serializer.data)


    @swagger_auto_schema(
        operation_description= "DELETE USER SKILL",
        request_body= openapi.Schema(
            type = openapi.TYPE_OBJECT,
            properties={
                'id': openapi.Schema(type = openapi.TYPE_INTEGER),
            }
        ),
        responses={
            200: "DELETE OK",
            404: "NOT FOUND"
        }
    )
    def delete(self, request):
        # permission

        data = request.body
        id = data.get('id', None)

        user_skill = UserSkill.objects.filter(pk = id)
        if not user_skill:
            return Response("not found", status=status.HTTP_404_NOT_FOUND)

        try:
            user_skill.delete()
            return Response("Delete successful", status=status.HTTP_200_OK)
        except:
            return Response("Delete unsuccessful", status=status.HTTP_400_BAD_REQUEST)