from django.urls import path 
from .views import APIPermission
urlpatterns = [
    path('',APIPermission.as_view({'get':'list'}))
]
