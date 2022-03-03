from distutils.log import Log
from re import L
from sys import exec_prefix
from rest_framework.viewsets import ViewSet
from .serializers import DetailRatingSerializer
from app.models import Rating, LogRating, DetailRating, User

from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import orjson
from django.db.models import F
import datetime

class DetailRatingViewSet(ViewSet):
    def list(self, request):
        user_id_assessor = self.request.query_params.get('user_id_assessor', None)
        user_id_rated = self.request.query_params.get('user_id_rated', None)

        detail_ratings = DetailRating.objects.all().annotate(
            assessor_name = F('user_id_assessor__username'),
            assessor_position = F('user_id_assessor__position'),
            user_id_rated = F('rating_id__user_id_rated'),
            rated_name = F('rating_id__user_id_rated__username'),
            rated_position = F('rating_id__user_id_rated__position'),
            session_rating = F('rating_id__session_rating')
        ).values(
            'id',
            'user_id_assessor',
            'assessor_name',
            'assessor_position',
            'user_id_rated',
            'rated_name',
            'rated_position',
            'score',
            'description',
            'session_rating'
        )

        if user_id_assessor:
            detail_ratings = detail_ratings.filter(user_id_assessor = user_id_assessor)
        if user_id_rated:
            detail_ratings = detail_ratings.filter(user_id_rated = user_id_rated)

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
        rating = Rating.objects.filter(pk = rating_id).first()
        
        #Get user rated
        user_rated= rating.user_id_rated
        #user_rated = User.objects.get(pk = user_rated_id)

        #Create DetailRating
        detail_rating = DetailRating.objects.create(
            user_id_assessor = user_assessor,
            rating_id = rating,
            description = description,
            score = score
        )

        if not detail_rating:
            return Response("Failed", status=status.HTTP_400_BAD_REQUEST)
        else:
            #create log
            LogRating.objects.create(
                detail_rating_id = detail_rating,
                user_id_assessor = user_assessor,
                user_id_rated = user_rated,
                score = score,
                description = description,
                action = "Create",
                update_at = datetime.datetime.now()
            )
            return Response("Create successful", status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        detail_rating = DetailRating.objects.get(pk = pk)
        if not detail_rating:
            return Response("Detail rating not found", status=status.HTTP_404_NOT_FOUND)
        
        if not request.body:
            return Response("Data invalid", status=status.HTTP_204_NO_CONTENT)
        data = orjson.loads(request.body)

        user_assessor_id = data.get("user_id_assessor", None)
        rating_id = data.get("rating_id", None)
        description = data.get("description", None)
        score = data.get("score", None)

        user_assessor = User.objects.get(pk = user_assessor_id)
        rating = Rating.objects.get(pk = rating_id)

        #update
        if user_assessor:
            detail_rating.user_id_assessor = user_assessor
        if rating_id:
            detail_rating.rating_id = rating
        if description:
            detail_rating.description = description
        if score:
            detail_rating.score = score
        detail_rating.save()

        #get user rated
        user_rated = rating.user_id_rated
       

        #create log
        LogRating.objects.create(
            detail_rating_id = detail_rating,
            user_id_assessor = user_assessor,
            user_id_rated = user_rated,
            score = score,
            description = description,
            action = "Update",
            update_at = datetime.datetime.now()
        )

        serializer = DetailRatingSerializer(detail_rating)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        detail_rating = DetailRating.objects.get(pk = pk)
        if not detail_rating:
            return Response("Detail rating not found", status=status.HTTP_404_NOT_FOUND)

        try:
            LogRating.objects.create(
                detail_rating_id = detail_rating,
                action = "Delete",
                update_at = datetime.datetime.now()
            )
            detail_rating.delete()
            return Response("Delete successful", status=status.HTTP_200_OK)
        except:
            return Response("Delete unsuccessful", status=status.HTTP_400_BAD_REQUEST)