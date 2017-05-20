from database.models import GliaUser
from rest_framework import authentication
from rest_framework import permissions

class GliaPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == "POST":
            return True 
        return False

    def has_object_permission(self, request, view, obj):
        if request.method == "POST":
            return True 
        return False

class GliaGetPermission(permissions.BasePermission):

    def has_permission(self, request,view):
        if request.method == "GET" or request.method == "PUT":
            return True 
        return False

    def has_object_permission(self, request,view):
        if request.method == "GET" or request.method == "PUT":
            return True 
        return False