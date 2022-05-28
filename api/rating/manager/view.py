from http.client import OK
import orjson
from rest_framework.response import Response
from api.base.api_view import BaseAPIView
from core.models import Rating, LogRating , User
from ..serializes import  RatingSerializer, LogRatingSerializer 
from rest_framework import status 
from datetime import datetime
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
class APIRating(BaseAPIView):
    queryset = Rating.objects.all()

    @swagger_auto_schema(
        operation_description="LIST ALL RATING",
        responses={
            200: "OK"
        }
        )
    def list(self, requesst, *args, **kwargs):
        
        rating = Rating.objects.all()

        data = RatingSerializer(rating,many = True).data

        return Response(data,200)
    

    @swagger_auto_schema(
        operation_description= "CREATE RAITNG ",
        request_body= openapi.Schema(
            type= openapi.TYPE_OBJECT,
            properties= {
                'user_id_rated': openapi.Schema(type = openapi.TYPE_STRING),
                'session_rating': openapi.Schema(type = openapi.TYPE_STRING),
                'description': openapi.Schema(type = openapi.TYPE_STRING),
            }
        ),
        responses=
        {
            201 : "CREATE OK",
            400 : "MISSING DATA",
            401 : "UNANTHENTICATION",
            404 : "NOT FOUND"
        }
    )
    def create(self,request,*args,**kwargs):
        
        data  = orjson.loads(request.body)

        data_dict = {
            'user_id_rated': request.data.get('user_id_rated',None),
            'session_rating': request.data.get('session_rating',None),
            'description' : request.data.get('description',None),
            'score' : None,
            'create_at' : datetime.now(),
            'create_by' : request.user.username
        }
                        
        if data_dict['user_id_rated']:
            try:
                data_dict['user_id_rated']= User.objects.get(id = data_dict['user_id_rated'])
                if not data_dict['score']:
                    return Response(
                        data =  "MISSING DATA SCORE",
                        status=  status.HTTP_400_BAD_REQUEST
                    )
                rating = Rating.objects.create(**data_dict)
                serializer_data = RatingSerializer(rating).data
                return Response(
                    data =  serializer_data,
                    status= status.HTTP_201_CREATED
                )
            except User.DoesNotExist: 
                return Response(data =  "NOT FOUND USER",
                                status= status.HTTP_404_NOT_FOUND)

        else:
            return Response(
                        data =  "MISSING DATA SCORE",
                        status=  status.HTTP_400_BAD_REQUEST
                    )

        