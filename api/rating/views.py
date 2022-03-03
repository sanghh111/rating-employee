from distutils.log import Log
from re import L
from sys import exec_prefix
from rest_framework.viewsets import ViewSet
from .serializers import DetailRatingSerializer, LogRatingSerializer, RatingSerializer
from app.models import Rating, LogRating, DetailRating, User

from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import orjson
from django.db.models import F
import datetime

class RatingViewSet(ViewSet):
    def list(self, request):
        ratings = Rating.objects.all().values()
        return Response(ratings)

    def rating(self, request):
        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        data = orjson.loads(request.body)

        user_id_rated = data.get("user_id_rated", None)
        session = data.get("session_rating", None)

        user_rated = User.objects.get(pk = user_id_rated)

        rating = Rating.objects.create(
            user_id_rated = user_rated,
            session_rating = session
        )
        if not rating:
            return Response("Create unsuccessful", status=status.HTTP_400_BAD_REQUEST)
        return Response("Create successfull", status=status.HTTP_201_CREATED)

class LogRatingViewSet(ViewSet):
    def list(self, request):
        user_id_assessor = self.request.query_params.get('user_id_assessor', None)
        user_id_rated = self.request.query_params.get('user_id_rated', None)

        log_ratings = LogRating.objects.all().annotate(
            log_rating_id = F('id'),
            assessor_name = F('user_id_assessor__username'),
            assessor_position = F('user_id_assessor__position'),
            rated_name = F('user_id_rated__username'),
            rated_position = F('user_id_rated__position'),
        ).values(
            'log_rating_id',
            'detail_rating_id',
            'user_id_assessor',
            'assessor_name',
            'assessor_position',
            'user_id_rated',
            'rated_name',
            'rated_position',
            'score',
            'description',
            'action',
            'update_at',
        )
        if not log_ratings:
            return Response("Data not found", status = status.HTTP_404_NOT_FOUND)

        if user_id_assessor:
            log_ratings = log_ratings.filter(user_id_assessor = user_id_assessor)
        if user_id_rated:
            log_ratings = log_ratings.filter(user_id_rated = user_id_rated)
        
        return Response(log_ratings)