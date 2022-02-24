from rest_framework import serializers
from ..serializers import BasicSerializer

class GroupSkillSerializer(BasicSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    group_skill_name = serializers.CharField()


class SkillSerializer(BasicSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    skill_name = serializers.CharField()
    group_skill_id = GroupSkillSerializer()