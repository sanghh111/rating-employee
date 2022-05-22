import orjson
from rest_framework.response import Response
from api.base.api_view import BaseAPIView
from core.models import Rating, LogRating , User
from ..serializes import  RatingSerializer, LogRatingSerializer 
from rest_framework import status 
from datetime import datetime
class APIRating(BaseAPIView):
    queryset = Rating.objects.all()

    def list(self, requesst, *args, **kwargs):
        
        rating = Rating.objects.all()

        data = RatingSerializer(rating,many = True).data

        return Response(data,200)
    
    def create(self,request,*args,**kwargs):
        
        if not  request.body :
            return Response(data  = "NOT BODY",
                            status = status.HTTP_400_BAD_REQUEST)
        else:
            data  = orjson.loads(request.body)

            data_dict = {
                'user_id_rated': data.get('user_id_rated',None),
                'session_rating': data.get('session_rating',None),
                'description' : data.get('description',None),
                'score' : data.get('score',None),
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

        