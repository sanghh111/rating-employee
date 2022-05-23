import orjson
from core.models import User, Rating, LogRating
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import  ViewSet
from ..serializes import LogRatingSerializer,RatingSerializer,LogRatingNonRatingSerializer
from rest_framework.response import  Response
from django.db import models
from constant.score import SCORE
from datetime import datetime

class APIRatingDetail(ViewSet):
    
    permission_classes = [IsAuthenticated]

    def list(self,request,*args, **kwargs):
                
        priority = request.user.get_position()
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
        if not kwargs:
            serializer = RatingSerializer(rating, many= True).data
        else:
            try:
                rating = rating.get(**kwargs)
                data = RatingSerializer(rating).data
                data.update(log_rating = [])
                log_ratings = LogRating.objects.filter(rating_id = rating.id)
                for log_rating in log_ratings:
                    data_log_rating = LogRatingNonRatingSerializer(log_rating).data
                    data_log_rating.update(modify =  (log_rating.user_id_assessor == request.user)) 
                    data['log_rating'].append(data_log_rating)
            except Exception as e:
                return Response(
                    e,
                    404
                )

        return Response(
            data = data,
            status= status.HTTP_200_OK
        )

    """
        BODY
        {
            'id'
            'score'
            'description'
        }
    """

    def update(self,request, *args, **kwargs):
        if not request.body:
            return Response(data= "BODY NO DATA",status= 400)

        priority = self.request.user.get_position()        
        #LOAD DATA
        data = orjson.loads(request.body)
        id_rating = kwargs['pk']
        score = data.get('score',None)
        description = data.get('description',None)

        if score == None:
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
            log = LogRating.objects.get(user_id_assessor = request.user.id,
                              rating_id = id_rating)
        except LogRating.DoesNotExist:
            return Response(data = "NOT FOUND",status=status.HTTP_404_NOT_FOUND)

        log.score = score
        log.action = "UPDATE"
        log.updated_at = datetime.now()
        log.updated_by= request.user.username
        if description:
            log.description = description
        log.save()
        

        log_ratings = LogRating.objects.filter(rating_id = id_rating).values_list('weight','score')

        total_score = 0
        total_weight = 0
        for log_rating in log_ratings:
            total_score += ((SCORE.index(log_rating[1])+1) * log_rating[0])
            total_weight += log_rating[0]
        score  =  int(round(total_score/total_weight,0))-1
        rating.score = SCORE[score]
        rating.save()
        data = LogRatingSerializer(log).data
        return Response(data,200)

    """
    BODY
        {
            delete_parent = BOOL
        }
    """

    def destroy(self,request, *args, **kwargs):
        pass