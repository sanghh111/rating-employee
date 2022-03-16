from django.urls import path, include
from .views import UserViewSet
from .login import UserLoginViewSet

urlpatterns = [
    path('create/', UserViewSet.as_view({'post':'create'})),
    path('list/', UserViewSet.as_view({'get':'list'})),
    #path('login/', jwt_views.TokenObtainPairView.as_view(), name='login'),
    path('login/', UserLoginViewSet.as_view({'post':'post'})),
]