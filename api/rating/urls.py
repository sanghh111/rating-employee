from django.urls import path, include
from .views import RatingViewSet, LogRatingViewSet
from . detail import DetailRatingViewSet

urlpatterns = [
    path('list/', RatingViewSet.as_view({'get':'list'})),
    path('rating_user/', RatingViewSet.as_view({'post':'rating'})),

    path('detail-rating/list/', DetailRatingViewSet.as_view({'get':'list'})),
    path('detail-rating/create/', DetailRatingViewSet.as_view({'post':'create'})),
    path('detail-rating/update/', DetailRatingViewSet.as_view({'put':'update'})),
    path('detail-rating/delete/', DetailRatingViewSet.as_view({'delete':'delete'})),

    path('log-rating/list/', LogRatingViewSet.as_view({'get':'list'}))
]