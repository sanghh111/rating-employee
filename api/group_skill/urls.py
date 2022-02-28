from django.urls import path, include
from .views import GroupSkillViewSet, GroupSkillDetailViewSet, SkillViewSet, SkillDetailViewSet

urlpatterns = [
    path('list/', GroupSkillViewSet.as_view({'get':'list'})),
    path('create/', GroupSkillViewSet.as_view({'post':'create'})),
    path('detail/<int:pk>/', GroupSkillDetailViewSet.as_view({'get':'get_detail'})),
    path('skill/list/', SkillViewSet.as_view({'get':'list'})),
    path('skill/create/', SkillViewSet.as_view({'post':'create'})),
    path('skill/detail/<int:pk>/', SkillDetailViewSet.as_view({'get':'get_detail'}))
]   