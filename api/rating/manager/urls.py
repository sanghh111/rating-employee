from django.urls import path
from .view import APIRating
from .detail import APIDetailRating
urlpatterns = [
    path('list/',APIRating.as_view({'get':'list',
                                'post':'create'})),
    path('detail/',APIDetailRating.as_view({'get':'list'}))            
            ]