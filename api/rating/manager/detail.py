import orjson
from rest_framework.response import Response
from api.base.api_view import BaseAPIView
from core.models import Rating, LogRating , User
from ..serializes import  RatingSerializer, LogRatingSerializer 
from rest_framework import status 
from datetime import datetime

class APIDetailRating(BaseAPIView):
    queryset = Rating.objects.all()

    def list(self, request, *args, **kwargs):


        id = request.query_params.get()
        
        rating = Rating.objects.all()

        data = RatingSerializer(rating,many = True).data

        return Response(data,200)
    

