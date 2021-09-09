from rest_framework import permissions


class UpdataProfile(permissions.BasePermission):
    
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user == request.user


class UpdateTwitter(permissions.BasePermission):


    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.profile_user == request.user.profile



class UpdateComment(permissions.BasePermission):
    

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user == request.user