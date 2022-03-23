from django.urls import path, include
from .views import RoleViewSet

urlpatterns = [
    path('list/', RoleViewSet.as_view({'get':'list'})),
    path('create/', RoleViewSet.as_view({'post':'create'})),
    path('delete/', RoleViewSet.as_view({'delete':'delete'}))
]