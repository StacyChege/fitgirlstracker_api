from rest_framework import permissions
from .models import ExpertProfile

class IsExpert(permissions.BasePermission):
    """
    Custom permission to only allow expert users to post workouts.
    A user is considered an expert if their ExpertProfile is verified.
    """
    def has_permission(self, request, view):
        # A user must be authenticated to check for an expert profile
        if not request.user.is_authenticated:
            # Allow read-only access (GET, HEAD, OPTIONS) for anonymous users
            return request.method in permissions.SAFE_METHODS

        # For write access (POST, PUT, DELETE), the user must be a verified expert.
        try:
            return request.user.expertprofile.verified
        except ExpertProfile.DoesNotExist:
            # If the user doesn't have an expert profile, they can't be an expert
            return False
    
class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission to allow only the object's owner or an admin
    to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner or admin
        return obj.user == request.user or request.user.is_staff  
    