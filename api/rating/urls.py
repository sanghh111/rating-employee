from django.urls import path, include
from .views import RatingViewSet, DetailRatingViewSet, LogRatingViewSet

urlpatterns = [
    path('list/', RatingViewSet.as_view({'get':'list'})),
    path('rating_user/', RatingViewSet.as_view({'post':'rating'})),

    path('detail-rating/list/', DetailRatingViewSet.as_view({'get':'list'})),
    path('detail-rating/create/', DetailRatingViewSet.as_view({'post':'create'})),
    path('detail-rating/update/<int:pk>/', DetailRatingViewSet.as_view({'put':'update'})),

    path('log-rating/list/', LogRatingViewSet.as_view({'get':'list'}))
]