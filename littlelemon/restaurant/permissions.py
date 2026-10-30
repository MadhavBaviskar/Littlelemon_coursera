from rest_framework.permissions import BasePermission,SAFE_METHODS
class IsManagerOrReadOnly(BasePermission):
 def has_permission(self,request,view):
  return request.method in SAFE_METHODS or bool(request.user.is_authenticated and (request.user.is_staff or request.user.groups.filter(name="Manager").exists()))
