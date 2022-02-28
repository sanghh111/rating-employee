from django.urls import path, include

app_name = 'app'
urlpatterns = [
    path('group-skill/', include("api.group_skill.urls")),
    path('project/', include("api.project.urls")),
    # path('project-user-work/', include("project_user_work.urls")),
    # path('rating/', include("rating.urls")),
    # path('user/', include("user.urls")),
    # path('users-kill/', include("user_skill.urls")),
]