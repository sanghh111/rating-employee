from rest_framework.viewsets import ViewSet
from core.models import GroupSkill, Skill
from .serializers import GroupSkillSerializer, SkillSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import orjson
from django.db.models import F
from api.base.api_view import CustomAPIView

class GroupSkillDetailViewSet(CustomAPIView):

    queryset = GroupSkill.objects.all()

    def update(self, request):
        # permission

        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        data = orjson.loads(request.body)

        id = data.get("id", None)
        group_skill_name = data.get("group_skill_name", None)

        group_skill = GroupSkill.objects.filter(pk=id).first()
        if group_skill:
            if group_skill_name:
                group_skill.group_skill_name = group_skill_name

                serializer = GroupSkillSerializer(group_skill)
                return Response(serializer.data)
            else:
                return Response("Data errol", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Group skill invalid", status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        # permission
        request.user.verify_permission('delete_groupskill')

        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        data = orjson.loads(request.body)

        id = data.get("id", None)

        group_skill = GroupSkill.objects.filter(pk=id).first()
        if group_skill:
            try:
                group_skill.delete()
                return Response("Deleted", status=status.HTTP_200_OK)
            except:
                return Response("Delete unsuccessful", status=status.HTTP_400_BAD_REQUEST)
        return Response("Group skill not found", status=status.HTTP_404_NOT_FOUND)


class SkillDetailViewSet(CustomAPIView):

    queryset = Skill.objects.all()

    def get_detail(self, request):
        # permission

        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        data = orjson.loads(request.body)

        skill_id = data.get("skill_id", None)

        skill = Skill.objects.filter(pk = skill_id).annotate(
            skill_id=F('id'),
            skill_name=F('name'),
            group_skill_name=F('group_skill_id__group_skill_name'),
        ).values(
            'skill_id',
            'skill_name',
            'group_skill_name',
        ).first()
        if not skill:
            return Response("Errol", status=status.HTTP_404_NOT_FOUND)
        return Response(skill)
    
    def update(self, request):
        # permission

        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        data = orjson.loads(request.body)

        skill_id = data.get("skill_id", None)
        name = data.get("name", None)
        group_skill_id = data.get("group_skill_id", None)

        skill = Skill.objects.filter(pk = skill_id).first()
        if not skill:
            return Response("Skill not found", status=status.HTTP_404_NOT_FOUND)

        if name:
            skill.name = name
        if group_skill_id:
            skill.group_skill_id = group_skill_id
        return Response(skill)

    def delete(self, request):
        # permission
        request.user.verify_permission('delete_skill')

        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        data = orjson.loads(request.body)

        skill_id = data.get("skill_id", None)

        skill = Skill.objects.filter(pk=skill_id).first()
        if not skill:
            return Response("Skill not found", status=status.HTTP_404_NOT_FOUND)
        try:
            skill.delete()
            return Response("Deleted", status=status.HTTP_200_OK)
        except:
            return Response("Deleted unsuccessful", status=status.HTTP_400_BAD_REQUEST)