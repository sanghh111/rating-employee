from django.urls import path, include
from .views import UserSkillViewSet, UserSkillDetailViewSet

urlpatterns = [
    path('list/', UserSkillViewSet.as_view({'get':'list'})),
    path('create/', UserSkillViewSet.as_view({'post':'create'})),

    path('update/<int:pk>/', UserSkillDetailViewSet.as_view({'put':'update'})),
    path('delete/<int:pk>/', UserSkillDetailViewSet.as_view({'delete':'delete'}))
]