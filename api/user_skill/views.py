from rest_framework.viewsets import ViewSet
from .serializers import UserSkillSerializer
from app.models import UserSkill, Skill, User

from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import orjson
from django.db.models import F

class UserSkillViewSet(ViewSet):
    def list(self, request):
        skill_id = self.request.query_params.get('skill_id', None)
        user_id = self.request.query_params.get('user_id', None)
        year_of_experience = self.request.query_params.get('year_of_experience', None)
        level = self.request.query_params.get('level', None)

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
    
    def create(self, request, *args, **kwargs):
        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        data = orjson.loads(request.body)

        skill_id = data.get("skill_id", None)
        user_id = data.get("user_id", None)
        year_of_experience = data.get("year_of_experience", None)
        level = data.get("level", None)

        skill = Skill.objects.get(pk = skill_id)
        user = User.objects.get(pk = user_id)

        user_skill = UserSkill.objects.create(
            skill_id = skill,
            user_id = user,
            year_of_experience = year_of_experience,
            level = level
        )

        if not user_skill:
            return Response("Errol", status=status.HTTP_400_BAD_REQUEST)
        return Response("Create successful", status=status.HTTP_201_CREATED)

class UserSkillDetailViewSet(ViewSet):
    def update(self, request, pk):
        user_skill = UserSkill.objects.get(pk = pk)
        if not user_skill:
            return Response("User skill not found", status=status.HTTP_404_NOT_FOUND)
        
        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        data = orjson.loads(request.body)

        skill_id = data.get("skill_id", None)
        user_id = data.get("user_id", None)
        year_of_experience = data.get("year_of_experience", None)
        level = data.get("level", None)

        skill = Skill.objects.get(pk = skill_id)
        user = User.objects.get(pk = user_id)

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

    def delete(self, request, pk):
        user_skill = UserSkill.objects.get(pk = pk)
        if not user_skill:
            return Response("not found", status=status.HTTP_404_NOT_FOUND)
        
        try:
            user_skill.delete()
            return Response("Delete successful", status=status.HTTP_200_OK)
        except:
            return Response("Delete unsuccessful", status=status.HTTP_400_BAD_REQUEST)