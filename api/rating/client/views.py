from datetime import datetime
import orjson
from rest_framework.response import Response
from rest_framework import status
from ..serializes import LogRatingSerializer, RatingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from core.models import Rating, LogRating
from core.user.models import User
from django.db import models 
from constant.score  import SCORE
class APIRating(ViewSet):
    
    permission_classes = [IsAuthenticated]

    def list(self,request,*args, **kwargs):
        
        #EXPRESSION POSITION
        priority = self.request.user.get_position()
        #MEMBER    
        if priority == 1 :
            rating = Rating.objects.annotate(
                user_rated_id = models.F('user_id_rated__id') 
            ).filter(user_rated_id = self.request.user.id)
        #MANAGER
        elif priority == 2:
            list_user = User.objects.filter(position='API').values_list('id')
            rating = Rating.objects.filter(user_id_rated_id__in = list_user)
        #PRINCIPLE
        elif priority ==3:
            rating = Rating.objects.all()
        else:
            pass
        serializer = RatingSerializer(rating, many= True)
        return Response(
            data = serializer.data,
            status= status.HTTP_200_OK
        )
    
    #Create LOG RATING
    # BODY
    # {
    #   'id'         
    #   'score'
    #   'description'  
    # }
    def create(self,request,*args, **kwargs):
        if not request.body:
            return Response(data= "BODY NO DATA",status= 400)
        
        priority = self.request.user.get_position()        
        #LOAD DATA
        data = orjson.loads(request.body)
        id_rating = data.get('id',None)
        score = data.get('score',None)
        description = data.get('description',None)
    
        if id_rating == None or score == None:
            return Response(data = "Missing Data",status=400)
        

        if  score not in SCORE :
            return Response(data = "SCORE MUST BE ['D','C','B','A','S']",status= 400)

        priority = self.request.user.get_position()
        try:
            #MEMBER    
            if priority == 1 :
                rating = Rating.objects.annotate(
                    user_rated_id = models.F('user_id_rated__id') 
                ).get(user_rated_id = self.request.user.id,id=id_rating)
                weight =priority
            #MANAGER
            elif priority == 2:
                list_user = User.objects.filter(position='API').values_list('id')
                rating = Rating.objects.get(user_id_rated_id__in = list_user,id=id_rating)
                weight = priority
            #PRINCIPLE
            elif priority ==3:
                rating = Rating.objects.get(id = id_rating)
                weight = 4
            else:
                pass
        except Rating.DoesNotExist:
            return Response(
                data = "NOT FOUND",
                status = 404
            )
        try:
            LogRating.objects.get(user_id_assessor = request.user.id,
                              rating_id = id_rating)
            return Response(data = "CAN NOT CREATE LOGRATING",status=status.HTTP_409_CONFLICT)
        except LogRating.DoesNotExist:
            pass

        dict_log_rating = {
            'rating_id' : rating, 
            'score': score,
            'description': description,
            'action': 'Create', 
            'weight': weight,
            'created_at': datetime.now(),
            'created_by': request.user,
            'user_id_assessor': request.user
        }

        log_rating =  LogRating.objects.create(**dict_log_rating)
        serializer = LogRatingSerializer(log_rating)

        log_ratings = LogRating.objects.filter(rating_id = id_rating).values_list('weight','score')
        
        total_score = 0
        total_weight = 0
        for log_rating in log_ratings:
            total_score += ((SCORE.index(log_rating[1])+1) * log_rating[0])
            total_weight += log_rating[0]
        score  =  int(round(total_score/total_weight,0))-1
        rating.score = SCORE[score]
        rating.save()
        return Response(serializer.data,201)
    pass