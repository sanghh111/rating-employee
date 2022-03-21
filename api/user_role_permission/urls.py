from django.urls import path
from .views import UserRolePermissionViewSet

urlpatterns = [
    path('list/', UserRolePermissionViewSet.as_view({'get':'list'})),
]