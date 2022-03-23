from django.urls import path, include
from .views import UserRoleViewSet

urlpatterns = [
    path('list/', UserRoleViewSet.as_view({'get':'list'})),
    path('create/', UserRoleViewSet.as_view({'post':'create'})),
    path('update/', UserRoleViewSet.as_view({'put':'update'})),
    path('delete/', UserRoleViewSet.as_view({'delete':'delete'})),
]