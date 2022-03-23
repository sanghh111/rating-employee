from rest_framework.viewsets import ViewSet
from app.models import GroupSkill, Skill
from .serializers import GroupSkillSerializer, SkillSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import orjson
from django.db.models import F
from api.base.api_view import BaseAPIView

class GroupSkillViewSet(BaseAPIView):
    def list(self, request):
        # permission
        request.user.verify_permission('view_groupskill')

        group_skill_id = self.request.query_params.get("id", None)
        group_skill_name = self.request.query_params.get("name", None)

        group_skills = GroupSkill.objects.all()

        if group_skill_id:
            group_skills = group_skills.filter(id=group_skill_id)
        if group_skill_name:
            group_skills = group_skills.filter(group_skill_name__contains=group_skill_name)

        serializer = GroupSkillSerializer(group_skills, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        # permission
        request.user.verify_permission('add_groupskill')

        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        else:
            data = orjson.loads(request.body)

        group_skill_name = data.get('group_skill_name', None)

        group_skill = GroupSkill.objects.create(
            group_skill_name = group_skill_name
        )

        if group_skill:
            return Response("Create successful", status=status.HTTP_201_CREATED)
        else:
            return Response("Errol", status=status.HTTP_400_BAD_REQUEST)

class SkillViewSet(BaseAPIView):
    def list(self, request):
        # permission
        request.user.verify_permission('view_skill')

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
        

    def create(self, request, *args, **kwargs):
        # permission
        request.user.verify_permission('add_groupskill')
        
        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        
        data = orjson.loads(request.body)
        name = data.get('name', None)
        group_skill_id = data.get('group_skill_id')

        group_skill = GroupSkill.objects.filter(pk = group_skill_id)

        if group_skill:
            skill = Skill.objects.create(
                name = name,
                group_skill_id = group_skill
            )
            if not skill:
                return Response("Errol", status=status.HTTP_400_BAD_REQUEST)
            return Response("Create successful", status=status.HTTP_201_CREATED)     
        else:
            return Response("Data errol", status=status.HTTP_400_BAD_REQUEST)