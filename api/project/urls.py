from django.urls import path , include

urlpatterns = [
    # path('',include('user.urls'),
    path('manager/',include('api.project.manager.urls'))
    
]
