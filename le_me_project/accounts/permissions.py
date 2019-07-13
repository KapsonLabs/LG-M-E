from rest_framework.permissions import BasePermission
from .models import User

class AdminPermissions(BasePermission):

    def has_permission(self, request):
        return request.user.is_administrator and request.user.is_active