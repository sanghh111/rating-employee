from app.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GroupSkillSerializer



class GroupSkillAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            query = GroupSkill.objects.filter(pk=pk).first()
            serializer = GroupSkillSerializer(query, many=False)
        else:
            query = GroupSkill.objects.all()
            serializer = GroupSkillSerializer(query, many=True)
        return Response(serializer.data)
    def post(self, request):
        group_skill_name = request.data.get("group_skill_name")
        if group_skill_name is None:
            return  Response("{msg : group_skill_name is none}")

