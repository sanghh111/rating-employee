from django.urls import path
from .views import APIRating 
from .detail import APIRatingDetail
urlpatterns = [
    path('',APIRating.as_view({'get': 'list',
                                'post':'create'})),
    path('<int:pk>/',APIRatingDetail.as_view({
        'get':'list',
        'put': 'update',
        'delete': 'destroy'
    }))
]
