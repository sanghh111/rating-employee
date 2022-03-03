from django.urls import path, include
from .detail import ProjecUserWorkDetailViewSet
from .views import ProjectUserWorkViewSet

urlpatterns = [
    path('list/', ProjectUserWorkViewSet.as_view({'get':'list'})),
    path('create/', ProjectUserWorkViewSet.as_view({'post':'create'})),

    path('update/<int:pk>/', ProjecUserWorkDetailViewSet.as_view({'put':'update'})),
    path('delete/<int:pk>/', ProjecUserWorkDetailViewSet.as_view({'delete':'delete'}))
]