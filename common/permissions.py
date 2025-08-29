# common/permissions.py
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerForPatients(BasePermission):
    def has_object_permission(self, request, view, obj):
        return getattr(obj, "created_by_id", None) == request.user.id
