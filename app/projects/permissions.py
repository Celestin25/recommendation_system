from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsInvitee(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.invitee_email == request.user.email
