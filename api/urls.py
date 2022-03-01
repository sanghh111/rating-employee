from django.urls import path, include

app_name = 'app'
urlpatterns = [
    path('group-skill/', include("api.group_skill.urls")),
    path('project/', include("api.project.urls")),
    path('user/', include("api.user.urls")),
    # path('project-user-work/', include("project_user_work.urls")),
    # path('rating/', include("rating.urls")),
    
    path('user-skill/', include("api.user_skill.urls")),
]