from django.db import models
from ..user.models import User

class Rating(models.Model):
    user_id_rated = models.ForeignKey(User, on_delete=models.CASCADE)
    session_rating = models.DateField()

class DetailRating(models.Model):
    user_id_assessor = models.ForeignKey(User, on_delete=models.CASCADE)
    rating_id = models.ForeignKey(Rating, on_delete=models.CASCADE)
    score = models.IntegerField()
    description = models.TextField(blank=True, null=True)

class LogRating(models.Model):
    detail_rating_id = models.ForeignKey(DetailRating, on_delete=models.CASCADE)
    user_id_assessor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_assessor", default=0, null= True)
    user_id_rated = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_rated", default=0, null= True)
    score = models.IntegerField(default=0, null= True)
    description = models.TextField(blank=True, null=True)
    action = models.CharField(max_length=50, default='update')
    updated_at = models.DateTimeField(auto_now_add=True, blank = True, null = True)
    updated_by = models.CharField(max_length=50, blank = True, null = True, default='')
