from rest_framework import serializers
from ..serializers import BasicSerializer
from ..user.serializers import UserSerializer
from ..group_skill.serializers import SkillSerializer

class UserSkillSerializer(BasicSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    skill_id = SkillSerializer()
    user_id = UserSerializer()
    year_of_experience = serializers.IntegerField()
    level = serializers.CharField()
