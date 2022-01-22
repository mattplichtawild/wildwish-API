from rest_framework import permissions

class IsAdminOrSelf(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        
        ## return True is the user is the one making the request or if is superuser
        return obj == request.user or request.user.is_superuser