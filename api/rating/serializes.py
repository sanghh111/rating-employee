from email.policy import default
from api.serializers import BasicSerializer
from api.user.serializers import UserSerializer
from rest_framework import serializers



class RatingSerializer(BasicSerializer):
    id = serializers.IntegerField()
    user_id_rated = UserSerializer()
    session_rating = serializers.DateField()
    description = serializers.CharField()
    score =  serializers.CharField()
    created_at = serializers.DateField()
    created_by = serializers.CharField()
    updated_at  = serializers.DateField()
    updated_by = serializers.CharField()

class LogRatingSerializer(BasicSerializer):

    rating_id = RatingSerializer()
    user_id_assessor = UserSerializer()
    score = serializers.CharField()
    description = serializers.CharField()
    action = serializers.CharField()
    created_at = serializers.DateTimeField()
    created_by = serializers.CharField()
    updated_at  = serializers.DateTimeField()
    updated_by = serializers.CharField()
    weight =  serializers.IntegerField()


class LogRatingNonRatingSerializer(BasicSerializer):
    
    rating_id = serializers.StringRelatedField()
    user_id_assessor = UserSerializer()
    score = serializers.CharField()
    description = serializers.CharField()
    action = serializers.CharField()
    created_at = serializers.DateTimeField()
    created_by = serializers.CharField()
    updated_at  = serializers.DateTimeField()
    updated_by = serializers.CharField()
    weight =  serializers.IntegerField()