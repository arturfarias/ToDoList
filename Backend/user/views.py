from rest_framework import viewsets
from django.contrib.auth.models import User
from user.serializers import UserRequestSerializer, UserResponseSerializer
from user.permissions import IsAdminOrSelfOrAuthenticated 
from utils.auto_swagger import auto_swagger

@auto_swagger(UserRequestSerializer, UserResponseSerializer)
class UserViewset(viewsets.ModelViewSet):
    """ CRUD para usuarios. """
    queryset = User.objects.all()
    serializer_class = UserRequestSerializer
    permission_classes = [IsAdminOrSelfOrAuthenticated]


