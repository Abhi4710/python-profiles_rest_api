from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allows user to update own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to update their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """"Allows user to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to update their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id

