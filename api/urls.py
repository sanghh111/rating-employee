from django.urls import path, include

app_name = 'core'
urlpatterns = [
    path('group-skill/', include("api.group_skill.urls")),
    path('project', include("api.project.urls")),
    path('project-user-work/', include("api.project_user_work.urls")),
    # path('user/', include("api.user.urls")),
    # path('rating', include("api.rating.urls")),
    # path('user-skill/', include("api.user_skill.urls")),
    # path('role/', include("api.role.urls")),
    # path('user-role/', include("api.user_role.urls")),
    # path('user-role-permission/', include("api.user_role_permission.urls")),
    # path('permission/', include("api.permission.urls")),   
]