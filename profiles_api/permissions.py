from rest_framework import permissions 

class UpdateOwnProfile(permissions.BasePermission):
    """User to edit own profile"""

    def has_object_permission(self, request, view, obj):
        """Check useris trying to edit own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True 
        
        return obj.id == request.user.id 