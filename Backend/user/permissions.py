from rest_framework import permissions

class IsAdminOrSelfOrAuthenticated(permissions.BasePermission):
    """
    Validar se possui permisão de Admin ou esta acessando seus proprios dados.
    Post pode ser acessado por todos.
    """

    def has_permission(self, request, view):
        if(request.method == 'POST'):
            return True
        return request.user and request.user.is_authenticated


    def has_object_permission(self, request, view, obj):
        if(request.user.is_staff):
            return True
        return obj == request.user