from django.urls import path, include
from .views import UserSkillViewSet
from .detail import UserSkillDetailViewSet

urlpatterns = [
    path('list/', UserSkillViewSet.as_view({'get':'list'})),
    path('create/', UserSkillViewSet.as_view({'post':'create'})),
    path('update/', UserSkillDetailViewSet.as_view({'put':'update'})),
    path('delete/', UserSkillDetailViewSet.as_view({'delete':'delete'}))
]