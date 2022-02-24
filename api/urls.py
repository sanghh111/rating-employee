
from django.urls import path, include

urlpatterns = [
    path('groupskill/', include("group_skill.urls")),
    path('project/', include("project.urls")),
    path('projectuserwork/', include("project_user_work.urls")),
    path('rating/', include("rating.urls")),
    path('user/', include("user.urls")),
    path('userskill/', include("userskill.urls")),
]