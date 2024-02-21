from rest_framework import permissions

class IsBorrowerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.borrower.id == request.user.id or request.user.is_superuser