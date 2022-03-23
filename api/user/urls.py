from django.urls import path, include
from .views import UserViewSet
from .login import UserLoginViewSet
from .detail import UserDetailViewSet

urlpatterns = [
    path('create/', UserViewSet.as_view({'post':'create'})),
    path('list/', UserViewSet.as_view({'get':'list'})),
    path('login/', UserLoginViewSet.as_view({'post':'post'})),
    path('reset-password/', UserDetailViewSet.as_view({'post':'reset_password'})),
]