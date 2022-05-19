from django.urls import path ,include
from .views import APIPermission
urlpatterns = [
    path('',APIPermission.as_view({'get':'list'})),
    path('role/', include("api.permission.role.urls")),
    path('user/',include("api.permission.user.urls"))
]
