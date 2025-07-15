from rest_framework.permissions import BasePermission

class CanValidatePermissionOrHoliday(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.user.role == 'rh' and obj.status == 'pending'
        )
