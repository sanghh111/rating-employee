from operator import length_hint
from django.db import models
from ..user.models import User

class Rating(models.Model):
    user_id_rated = models.ForeignKey(User, on_delete=models.CASCADE)
    session_rating = models.TextField(null=True,max_length=100)

    score = models.CharField(null= True,max_length= 10)
    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, db_column='created_at', blank=True, null=True,
                                      verbose_name=('Created at'))
    updated_at = models.DateTimeField(db_column='modified_at', blank=True, null=True,
                                      verbose_name=('Updated at'))
    created_by = models.CharField(max_length=100, db_column='created_by', blank=True, null=True, default='',
                                  verbose_name=('Created by'))
    updated_by = models.CharField(max_length=100, db_column='modified_by', blank=True, null=True, default='',
                                  verbose_name=('Updated by'))
    class Meta:
        db_table = "rating"

        
class LogRating(models.Model):
    rating_id = models.ForeignKey(Rating,related_name='raing_id', on_delete=models.CASCADE,null= True)
    user_id_assessor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_assessor", default=0, null= True)
    score = models.CharField(default=0, null= True,max_length= 10)
    description = models.TextField(blank=True, null=True)
    action = models.CharField(max_length=50, default= "CREATE")

    created_at = models.DateTimeField(auto_now_add=True, db_column='created_at', blank=True, null=True,
                                      verbose_name=('Created at'))
    updated_at = models.DateTimeField(db_column='modified_at', blank=True, null=True,
                                      verbose_name=('Updated at'))
    created_by = models.CharField(max_length=100, db_column='created_by', blank=True, null=True, default='',
                                  verbose_name=('Created by'))
    updated_by = models.CharField(max_length=100, db_column='modified_by', blank=True, null=True, default='',
                                  verbose_name=('Updated by'))
    weight = models.IntegerField(null = True)
    class Meta:
        db_table = "log_rating"