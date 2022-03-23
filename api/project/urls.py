from django.urls import path, include
from .views import ProjectViewSet
from .detail import ProjectDetailViewSet
urlpatterns = [
    path('list/', ProjectViewSet.as_view({'get':'list'})),
    path('create/', ProjectViewSet.as_view({'post':'create'})),
    path('detail/update/', ProjectDetailViewSet.as_view({'put':'update'})),
    path('detail/delete/', ProjectDetailViewSet.as_view({'delete':'delete'}))
]