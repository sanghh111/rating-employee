from django.urls import path
from .views import *


urlpatterns = [
    path('group-skill/', GroupSkillAPIView.as_view()),
    path('group-skill/', GroupSkillAPIView.as_view())

]