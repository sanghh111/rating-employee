import orjson
from rest_framework.response import Response
from api.base.api_view import BaseAPIView
from core.models import Rating, LogRating , User
from ..serializes import  RatingSerializer, LogRatingSerializer 
from rest_framework import status 
from datetime import datetime
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class APIDetailRating(BaseAPIView):
    queryset = Rating.objects.all()


    @swagger_auto_schema(
        operation_description="LIST ALL RATING",
        manual_parameters= [openapi.Parameter('id',openapi.IN_QUERY,type = openapi.TYPE_STRING)],
        responses={
            200: "OK"
        }
        )
    def list(self, request, *args, **kwargs):


        id = request.query_params.get()
        
        rating = Rating.objects.all()

        data = RatingSerializer(rating,many = True).data

        return Response(data,200)
    