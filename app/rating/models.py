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
    update_at = models.DateTimeField()