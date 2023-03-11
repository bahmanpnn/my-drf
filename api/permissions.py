from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUser(BasePermission):
    """
    Allows access only to superusers.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsStaffOrReadOnly(BasePermission):
    """
    Allow access safe methods for all users but all access for is_staff
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
        )


class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        # access to all user and request safe method
        if request.method in SAFE_METHODS:
            return True
        # all access to is_super or author of that object
        return bool(
            request.user.is_superuser or
            obj.author == request.user
        )


class IsSuperUserOrStaffReadOnly(BasePermission):
    # remember that it is has_permission but it work on detailuser api!! so we can use has_permission for detail pages!
    def has_permission(self, request, view):
        # access safe methods for user that is authenticated and is_staff
        if request.method in SAFE_METHODS and \
                request.user.is_authenticated and \
                request.user.is_staff:
            return True
        # access all method to is_super
        return bool(
            request.user.is_superuser
        )
