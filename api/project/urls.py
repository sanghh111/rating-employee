from django.urls import path , include

urlpatterns = [
    path('',include('api.project.user.urls')),
    path('manager/',include('api.project.manager.urls'))
    
]
