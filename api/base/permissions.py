from rest_framework.permissions import DjangoModelPermissions

class IsActiveUser(DjangoModelPermissions):

    """
    allow access user Manager or higher or role user have access 
    """

    perms_map = {
        'GET': ['list_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['add_%(model_name)s'],
        'PUT': ['change_%(model_name)s'],
        'PATCH': ['change_%(model_name)s'],
        'DELETE': ['delete_%(model_name)s'],
    }

    def has_permission(self, request, view):

        if getattr(view, '_ignore_model_permissions', False):
            return True

        if not request.user or (
           not request.user.is_authenticated and self.authenticated_users_only):
            return False 


        queryset = self._queryset(view)
        perms = self.get_required_permissions(request.method, queryset.model)

        return bool(request.user.role_is_active(perms) or request.user.is_superuser or request.user.user_is_active(perms) )
