from rest_framework.permissions import BasePermission,DjangoModelPermissions

class IsManagerUser(DjangoModelPermissions):

    """
    allow access user Manager or higher or role user have access 
    """

    def has_permission(self, request, view):

        if getattr(view, '_ignore_model_permissions', False):
            return True

        if not request.user or (
           not request.user.is_authenticated and self.authenticated_users_only):
            return False 


        queryset = self._queryset(view)
        perms = self.get_required_permissions(request.method, queryset.model)
        print('perms: ', perms)

        return bool(request.user.has_perms(perms) or request.user.rank == 'MANAGER' or request.user.is_superuser )
