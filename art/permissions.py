from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):       
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.artist.user == request.user
    

class ProfileHolderOrReadOnly(permissions.BasePermission):
    """
    Allow only the artist to edit and delete their profile.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user == request.user     