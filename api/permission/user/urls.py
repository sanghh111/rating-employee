from django.urls import path
from .views import APIUserPermission
urlpatterns = [
    path('create',APIUserPermission.as_view({
            'post':'create'
    }))
]
