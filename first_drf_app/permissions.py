from rest_framework.permissions import BasePermission, IsAuthenticated


class CustomIsAuthenticated(IsAuthenticated):
    def has_permission(self, request, view):
        print("*********************check permission*************************")
        return super().has_permission(request, view)
    
    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)