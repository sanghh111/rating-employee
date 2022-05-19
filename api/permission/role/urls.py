from django.urls import path, include
from .views import RolePermissionViewSet

urlpatterns = [
    path('list/', RolePermissionViewSet.as_view({'get':'list'})),
    path('create/', RolePermissionViewSet.as_view({'post':'create'})),
    path('update/', RolePermissionViewSet.as_view({'put':'update'})),
    path('delete/', RolePermissionViewSet.as_view({'delete':'delete'})),
]