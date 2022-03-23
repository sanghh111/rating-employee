from django.db import models
from ..user.models import User

class Rating(models.Model):
    user_id_rated = models.ForeignKey(User, on_delete=models.CASCADE)
    session_rating = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True, db_column='created_at', blank=True, null=True,
                                      verbose_name=('Created at'))
    updated_at = models.DateTimeField(auto_now=True, db_column='modified_at', blank=True, null=True,
                                      verbose_name=('Updated at'))
    created_by = models.CharField(max_length=100, db_column='created_by', blank=True, null=True, default='',
                                  verbose_name=('Created by'))
    updated_by = models.CharField(max_length=100, db_column='modified_by', blank=True, null=True, default='',
                                  verbose_name=('Updated by'))
    class Meta:
        db_table = "rating"

class DetailRating(models.Model):
    user_id_assessor = models.ForeignKey(User, on_delete=models.CASCADE)
    rating_id = models.ForeignKey(Rating, on_delete=models.CASCADE)
    score = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, db_column='created_at', blank=True, null=True,
                                      verbose_name=('Created at'))
    updated_at = models.DateTimeField(auto_now=True, db_column='modified_at', blank=True, null=True,
                                      verbose_name=('Updated at'))
    created_by = models.CharField(max_length=100, db_column='created_by', blank=True, null=True, default='',
                                  verbose_name=('Created by'))
    updated_by = models.CharField(max_length=100, db_column='modified_by', blank=True, null=True, default='',
                                  verbose_name=('Updated by'))
    class Meta:
        db_table = "detail_rating"
        
class LogRating(models.Model):
    detail_rating_id = models.ForeignKey(DetailRating, on_delete=models.CASCADE)
    user_id_assessor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_assessor", default=0, null= True)
    user_id_rated = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_rated", default=0, null= True)
    score = models.IntegerField(default=0, null= True)
    description = models.TextField(blank=True, null=True)
    action = models.CharField(max_length=50, default='update')

    created_at = models.DateTimeField(auto_now_add=True, db_column='created_at', blank=True, null=True,
                                      verbose_name=('Created at'))
    updated_at = models.DateTimeField(auto_now=True, db_column='modified_at', blank=True, null=True,
                                      verbose_name=('Updated at'))
    created_by = models.CharField(max_length=100, db_column='created_by', blank=True, null=True, default='',
                                  verbose_name=('Created by'))
    updated_by = models.CharField(max_length=100, db_column='modified_by', blank=True, null=True, default='',
                                  verbose_name=('Updated by'))
    class Meta:
        db_table = "log_rating"