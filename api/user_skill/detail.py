
from .serializers import UserSkillSerializer
from app.models import UserSkill, Skill, User

from rest_framework.response import Response
from rest_framework import status
import orjson
from django.db.models import F
from api.base.api_view import BaseAPIView
from app.views.models import UserRolePermission
class UserSkillDetailViewSet(BaseAPIView):
    def update(self, request, pk):
        # #permission
        user = self.user
        user.verify_permission('change_userskill')

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
        # #permission
        user = self.user
        user.verify_permission('delete_userskill')

        user_skill = UserSkill.objects.get(pk = pk)
        if not user_skill:
            return Response("not found", status=status.HTTP_404_NOT_FOUND)
        
        try:
            user_skill.delete()
            return Response("Delete successful", status=status.HTTP_200_OK)
        except:
            return Response("Delete unsuccessful", status=status.HTTP_400_BAD_REQUEST)