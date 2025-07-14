from rest_framework.permissions import BasePermission

class CanValidateTask(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.user.role == 'rh' and obj.status == 'pending'
        )
