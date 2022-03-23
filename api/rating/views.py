from re import L
from sys import exec_prefix
from rest_framework.viewsets import ViewSet
from app.models import Rating, LogRating, DetailRating, User

from rest_framework.response import Response
from rest_framework import status

import orjson
from django.db.models import F
import datetime
from api.base.authentication import TokenAuthentication
from api.base.api_view import BaseAPIView

class RatingViewSet(BaseAPIView):

    def list(self, request):
        # permission
        
        request.user.verify_permission('view_rating')

        ratings = Rating.objects.all().values()
        return Response(ratings)

    def rating(self, request):
        # permission
        
        request.user.verify_permission('add_rating')

        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        data = orjson.loads(request.body)

        user_id_rated = data.get("user_id_rated", None)
        session = data.get("session_rating", None)

        user_rated = User.objects.filter(pk = user_id_rated).first()

        rating = Rating.objects.create(
            user_id_rated = user_rated,
            session_rating = session
        )
        if not rating:
            return Response("Create unsuccessful", status=status.HTTP_400_BAD_REQUEST)
        return Response("Create successfull", status=status.HTTP_201_CREATED)

class LogRatingViewSet(BaseAPIView):
    def list(self, request):
        # permission
        
        request.user.verify_permission('view_lograting')

        user_id_assessor = self.request.query_params.get('user_id_assessor', None)
        user_id_rated = self.request.query_params.get('user_id_rated', None)

        log_ratings = LogRating.objects.annotate(
            log_rating_id = F('id'),
            assessor_name = F('user_id_assessor__username'),
            assessor_position_role = F('user_id_assessor__position_role'),
            rated_name = F('user_id_rated__username'),
            rated_position_role = F('user_id_rated__position_role'),
        ).values(
            'log_rating_id',
            'detail_rating_id',
            'user_id_assessor',
            'assessor_name',
            'assessor_position_role',
            'user_id_rated',
            'rated_name',
            'rated_position_role',
            'score',
            'description',
            'action',
            'updated_at',
            'updated_by'
        )
        if not log_ratings:
            return Response("Data not found", status = status.HTTP_404_NOT_FOUND)

        if user_id_assessor:
            log_ratings = log_ratings.filter(user_id_assessor = user_id_assessor)
        if user_id_rated:
            log_ratings = log_ratings.filter(user_id_rated = user_id_rated)
        
        return Response(log_ratings)