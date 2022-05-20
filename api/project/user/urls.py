from django.urls import path

from api.project.user.detail import APIProjectDetail
from .views import  APIProject
urlpatterns = [
    path('list',APIProject.as_view({'get':'list'})),
    path('list-detail',APIProjectDetail.as_view({'get':'list'}))
]
