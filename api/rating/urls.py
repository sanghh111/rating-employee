from django.urls import path, include 


urlpatterns = [
    path('-manager/',include('api.rating.manager.urls')),
    path('/',include('api.rating.client.urls')),
]
