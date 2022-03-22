from django.urls import path, include

app_name = 'app'
urlpatterns = [
    path('group-skill/', include("api.group_skill.urls")),
    path('project/', include("api.project.urls")),
    path('user/', include("api.user.urls")),
    path('project-user-work/', include("api.project_user_work.urls")),
    path('rating/', include("api.rating.urls")),
    path('user-skill/', include("api.user_skill.urls")),
    path('role/', include("api.role.urls")),
    path('role-permission/', include("api.role_permission.urls")),
    path('user-role-permission/', include("api.user_role_permission.urls")),

]