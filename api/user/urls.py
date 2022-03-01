from django.urls import path, include
from .views import UserViewSet

urlpatterns = [
    path('create/', UserViewSet.as_view({'post':'create'})),
    path('list/', UserViewSet.as_view({'get':'list'})),
]