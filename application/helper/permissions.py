# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import permissions

import authentication


# Custom Permissions
class UserAccessPermission(permissions.BasePermission):
    message = "Create, Update or Delete operations not allowed"

    def has_permission(self, request, view):
        # only admin user can add, update or delete an user
        return request.method in permissions.SAFE_METHODS or (request.user and request.user.is_admin)


class IsAdministrator(permissions.BasePermission):
    message = "View, Update and Delete operations not allowed!"

    def has_permission(self, request, view):
        return isinstance(request.user, authentication.models.AppUserModel)  and request.user.is_admin


class IsSelf(permissions.BasePermission):
    message = "View, Update and Delete operations not allowed!"

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return isinstance(request.user, authentication.models.AppUserModel) and request.user == obj


class IsSelfOrIsAdministrator(permissions.BasePermission):
    message = "View, Update and Delete operations not allowed!"

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return isinstance(
            request.user, authentication.models.AppUserModel) and (
                request.user == obj or request.user.is_admin)
