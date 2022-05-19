from django.urls import path
from .views import  APIProject
urlpatterns = [
    path('list',APIProject.as_view({'get':'list'}))
]
