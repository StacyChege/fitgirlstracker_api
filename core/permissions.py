from rest_framework import permissions

class IsExpert(permissions.BasePermission):
    """
    Custom permission to only allow expert users to post workouts.
    A user is considered an expert if their ExpertProfile is verified.
    """
    def has_permission(self, request, view):
        # Check if the user is authenticated and has a verified ExpertProfile
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated

        #  Write access (e.g., POST) is only for experts
        return request.user.expertprofile.verified
    
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
    