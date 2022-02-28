from rest_framework import serializers
from ..serializers import BasicSerializer

class SkillSerializer(BasicSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    name = serializers.CharField()
    #group_skill_id = GroupSkillSerializer()

class GroupSkillSerializer(BasicSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    group_skill_name = serializers.CharField()
    skills = SkillSerializer(source="skill_set", many = True)
