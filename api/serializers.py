from rest_framework import serializers

class BasicSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass
    def update(self, instance, validated_data):
        pass

class UserSerializer(BasicSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    position = serializers.CharField(required=False)
    rank = serializers.CharField(required=False)

class GroupSkillSerializer(BasicSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    group_skill_name = serializers.CharField()


class SkillSerializer(BasicSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    skill_name = serializers.CharField()
    group_skill_id = GroupSkillSerializer()

class UserSkillSerializer(BasicSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    skill_id = SkillSerializer()
    user_id = UserSerializer()
    year_of_experience = serializers.IntegerField()
    level = serializers.CharField()

class ProjectSerializer(BasicSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    project_name = serializers.CharField()
    description = serializers.CharField()
    date_start = serializers.DateField()
    date_end = serializers.DateField()
    tech_stack = serializers.CharField()

class ProjectUserWorkSerializer(BasicSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    project_id = ProjectSerializer()
    user_id = UserSerializer()
    position = serializers.CharField()
    work = serializers.CharField()
    achieves = serializers.CharField()

class RatingSerializer(BasicSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    user_id_rated = UserSerializer()
    session_rating = serializers.DateField()

class DetailRatingSerializer(BasicSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    user_id_accessor = UserSerializer()
    rating_id = RatingSerializer()
    description = serializers.CharField()
    score = serializers.IntegerField()

class LogRatingSerializer(BasicSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    detail_rating_id = DetailRatingSerializer(read_only=True, required=False)
    update_at = serializers.DateTimeField()
