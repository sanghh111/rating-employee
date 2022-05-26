from django.urls import path, include
from .views import GroupSkillViewSet, SkillViewSet
from .detail import GroupSkillDetailViewSet, SkillDetailViewSet

urlpatterns = [
    path('list/', GroupSkillViewSet.as_view({'get':'list'})),
    path('create/', GroupSkillViewSet.as_view({'post':'create'})),
    path('update/', GroupSkillDetailViewSet.as_view({'put':'update'})),
    path('delete/', GroupSkillDetailViewSet.as_view({'delete':'delete'})),

    path('skill/list/', SkillViewSet.as_view({'get':'list'})),
    path('skill/create/', SkillViewSet.as_view({'post':'create'})),
    path('skill/detail/<int:id>', SkillDetailViewSet.as_view({'get':'get_detail'})),
    path('skill/update/<int:id>', SkillDetailViewSet.as_view({'put':'update'})),
    path('skill/delete/<int:id>', SkillDetailViewSet.as_view({'delete':'delete'})),
]   