from rest_framework.permissions import BasePermission

class IsManagerUser(BasePermission):

    """
    allow access user Manager or higher
    """

    def has_permission(self, request, view):

        return bool(request.user.rank == "MANAGER" or request.user.is_supperuser)
        # return super().has_permission(request, view)    