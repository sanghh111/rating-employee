from distutils.log import Log
from re import L
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


class DetailRatingViewSet(ViewSet):
    def list(self, request):
        detail_ratings = DetailRating.objects.all().values()
        return Response(detail_ratings)

    def create(self, request, *args, **kwagrs):
        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        data = orjson.loads(request.body)

        user_assessor_id = data.get("user_id_assessor", None)
        rating_id = data.get("rating_id", None)
        description = data.get("description", None)
        score = data.get("score", None)

        user_assessor = User.objects.get(pk = user_assessor_id)
        rating = Rating.objects.get(pk = rating_id)

        detail_rating = DetailRating.objects.create(
            user_id_assessor = user_assessor,
            rating_id = rating,
            description = description,
            score = score
        )

        if not detail_rating:
            return Response("Failed", status=status.HTTP_400_BAD_REQUEST)
        else:
            LogRating.objects.create(
                detail_rating_id = detail_rating,
                update_at = datetime.datetime.now()
            )
            return Response("Create successful", status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        detail_rating = DetailRating.objects.get(pk = pk)
        if not detail_rating:
            return Response("User skill not found", status=status.HTTP_404_NOT_FOUND)
        
        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        data = orjson.loads(request.body)

        user_assessor_id = data.get("user_id_assessor", None)
        rating_id = data.get("rating_id", None)
        description = data.get("description", None)
        score = data.get("score", None)

        user_assessor = User.objects.get(pk = user_assessor_id)
        rating = Rating.objects.get(pk = rating_id)

        if user_assessor:
            detail_rating.user_id_assessor = user_assessor
        if rating_id:
            detail_rating.rating_id = rating
        if description:
            detail_rating.description = description
        if score:
            detail_rating.score = score

        LogRating.objects.create(
            detail_rating_id = detail_rating,
            update_at = datetime.datetime.now()
        )

        serializer = DetailRatingSerializer(detail_rating)
        return Response(serializer.data)

class LogRatingViewSet(ViewSet):
    def list(self, request):
        user_id_assessor = self.request.query_params.get('user_id_assessor', None)
        user_id_rated = self.request.query_params.get('user_id_rated', None)

        log_ratings = LogRating.objects.all().annotate(
            log_rating_id = F('id'),
            user_id_assessor =F('detail_rating_id__user_id_assessor'),
            assessor_name = F('detail_rating_id__user_id_assessor__username'),
            assessor_position = F('detail_rating_id__user_id_assessor__position'),
            user_id_rated = F('detail_rating_id__rating_id__user_id_rated'),
            rated_name = F('detail_rating_id__rating_id__user_id_rated__username'),
            rated_position = F('detail_rating_id__rating_id__user_id_rated__position'),
            score = F('detail_rating_id__score'),
            description = F('detail_rating_id__description')
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
            'update_at',
        )
        if not log_ratings:
            return Response("Data not found", status = status.HTTP_404_NOT_FOUND)

        if user_id_assessor:
            log_ratings = log_ratings.filter(user_id_assessor = user_id_assessor)
        if user_id_rated:
            log_ratings = log_ratings.filter(user_id_rated = user_id_rated)
        
        return Response(log_ratings)