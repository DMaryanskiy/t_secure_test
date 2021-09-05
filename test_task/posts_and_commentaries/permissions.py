"Модуль для определения собственных пермиссий"

from rest_framework import status, permissions
from rest_framework.permissions import BasePermission
from rest_framework.response import Response


class IsOwnerOrReadOnly(BasePermission):
    "Уровень доступа 'Владелец или только для чтения'"
    message = Response(status=status.HTTP_403_FORBIDDEN)

    def has_object_permission(self, request, view, obj):
        return request.user == obj.author or request.method in permissions.SAFE_METHODS
