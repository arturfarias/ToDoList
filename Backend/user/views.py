from rest_framework import viewsets
from django.contrib.auth.models import User
from user.serializers import UserSerializer

class UserViewset(viewsets.ModelViewSet):
    """ CRUD para usuarios. """
    queryset = User.objects.all()
    serializer_class = UserSerializer



