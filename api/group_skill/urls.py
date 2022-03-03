from django.urls import path, include
from .views import GroupSkillViewSet, SkillViewSet
from .detail import GroupSkillDetailViewSet, SkillDetailViewSet

urlpatterns = [
    path('list/', GroupSkillViewSet.as_view({'get':'list'})),
    path('create/', GroupSkillViewSet.as_view({'post':'create'})),
    path('detail/<int:pk>/', GroupSkillDetailViewSet.as_view({'get':'get_detail'})),
    path('update/<int:pk>/', GroupSkillDetailViewSet.as_view({'put':'update'})),
    path('delete/<int:pk>/', GroupSkillDetailViewSet.as_view({'delete':'delete'})),

    path('skill/list/', SkillViewSet.as_view({'get':'list'})),
    path('skill/create/', SkillViewSet.as_view({'post':'create'})),
    path('skill/detail/<int:pk>/', SkillDetailViewSet.as_view({'get':'get_detail'})),
    path('skill/update/<int:pk>/', SkillDetailViewSet.as_view({'put':'update'})),
    path('skill/delete/<int:pk>/', SkillDetailViewSet.as_view({'delete':'delete'})),
]   