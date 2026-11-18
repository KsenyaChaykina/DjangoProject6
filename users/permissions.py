from rest_framework import permissions

class UserIsModerator(permissions.BasePermission):
    """ Проверяет, является ли пользователь модератором. """

    def has_permission(self, request, view):
        return request.user.groups.filter(name='Модераторы').exists()

class UserIsOwner(permissions.BasePermission):
    """ Проверяет, является ли пользователь владельцем уроки или курса. """

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
