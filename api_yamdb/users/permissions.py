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
        return bool(request.method in SAFE_METHODS
                    or request.user == obj.author
                    or request.user and request.user.is_authenticated
                    and (request.user.role in ['moderator', 'admin']
                         or request.user.is_superuser)
                    )


class IsAdminOrReadOnly(BasePermission):
    """
    Only admin can modify.
    """

    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS
                    or request.user and request.user.is_authenticated
                    and (request.user.role == 'admin'
                         or request.user.is_superuser)
                    )


class IsAdminUser(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated
                    and (request.user.role == 'admin'
                         or request.user.is_staff)
                    )


class IsUserAccountOwner(BasePermission):
    """
    Allows access to modify account owner to modify his account.
    """

    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_authenticated
                    and request.user == obj)
