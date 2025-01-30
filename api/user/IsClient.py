
from rest_framework import permissions


class IsClient(permissions.BasePermission):
    message = 'You are not a client'

    def has_permission(self, request, view):
         if request.user:
              print(request.user.type)
              if request.user.type == 'client':
               return True
