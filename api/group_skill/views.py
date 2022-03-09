from rest_framework.viewsets import ViewSet
from app.models import GroupSkill, Skill
from .serializers import GroupSkillSerializer, SkillSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import orjson
from django.db.models import F

class GroupSkillViewSet(ViewSet):
    def list(self, request):
        group_skills = GroupSkill.objects.all()
        serializer = GroupSkillSerializer(group_skills, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
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


class SkillViewSet(ViewSet):
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
        

    def create(self, request, *args, **kwargs):
        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        
        data = orjson.loads(request.body)
        name = data.get('name', None)
        group_skill_id = data.get('group_skill_id')

        group_skill = GroupSkill.objects.get(pk = group_skill_id)
        print(group_skill)

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