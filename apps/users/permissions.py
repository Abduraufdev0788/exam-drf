from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    message = "siz admin emassiz"

    def has_permission(self, request, view):
        return request.user and request.user.is_admin
    
class IsUser(BasePermission):
    message = "siz user emassiz"

    def has_permission(self, request, view):
        return request.user and request.user.is_user
    

class IsDoctor(BasePermission):
    message = "siz doctor emassiz"

    def has_permission(self, request, view):
        return request.user and request.user.is_doctor
    
class IsOwner(BasePermission):
    message = "siz tizimga kirishga ruxsatingiz yoq"

    def has_object_permission(self, request, view, obj):
        if request.user.is_admin:
            return True
        
        if request.user.is_doctor:
            return obj.doctor.user == request.user
        
        if request.user.is_user:
            return obj.patient.user == request.user
        
        return False
    