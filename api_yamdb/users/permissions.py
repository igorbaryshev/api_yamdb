from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthorOrReadOnly(BasePermission):
    """
    Only authorized can create.
    Only author, moderator or admin can modify.
    """
    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS
                    or request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        if request.user == obj.author:
            return True

        if request.user.is_moderator or request.user.is_admin:
            return True

        return False


class IsAdminOrReadOnly(BasePermission):
    """
    Only admin can modify.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if (request.user and request.user.is_authenticated
           and request.user.is_admin):
            return True

        return False


class IsAdminUser(BasePermission):
    """
    Allows access only to admin users.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated
                    and request.user.is_admin)
