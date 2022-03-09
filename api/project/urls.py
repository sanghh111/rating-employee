from django.urls import path, include
from .views import ProjectViewSet
from .detail import ProjectDetailViewSet
urlpatterns = [
    path('list/', ProjectViewSet.as_view({'get':'list'})),
    path('create/', ProjectViewSet.as_view({'post':'create'})),
    path('detail/<int:pk>/', ProjectDetailViewSet.as_view({'get':'get_detail'})),
    path('detail/update/<int:pk>/', ProjectDetailViewSet.as_view({'put':'update'})),
    path('detail/delete/<int:pk>/', ProjectDetailViewSet.as_view({'delete':'delete'}))
]