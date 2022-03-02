from rest_framework import serializers
from ..serializers import BasicSerializer
from ..user.serializers import UserSerializer

class RatingSerializer(BasicSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    user_id_rated = UserSerializer()
    session_rating = serializers.DateField()

class DetailRatingSerializer(BasicSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    user_id_assessor = UserSerializer()
    rating_id = RatingSerializer()
    description = serializers.CharField()
    score = serializers.IntegerField()

class LogRatingSerializer(BasicSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    detail_rating_id = DetailRatingSerializer(read_only=True, required=False)
    update_at = serializers.DateTimeField()
