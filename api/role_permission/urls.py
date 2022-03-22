from django.urls import path, include
from .views import RolePermissionViewSet

urlpatterns = [
    path('list/', RolePermissionViewSet.as_view({'get':'list'})),
    path('create/', RolePermissionViewSet.as_view({'post':'create'})),
    path('delete/<int:pk>/', RolePermissionViewSet.as_view({'delete':'delete'}))
]