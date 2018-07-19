# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import permissions


# Custom Permissions
class UserAccessPermission(permissions.BasePermission):
    message = "Create, Update or Delete operations not allowed"

    def has_permission(self, request, view):
        # only admin user can add, update or delete an user
        return request.method in permissions.SAFE_METHODS or request.user.is_admin
