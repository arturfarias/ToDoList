from rest_framework import viewsets
from django.contrib.auth.models import User
from user.serializers import UserRequestSerializer, UserResponseSerializer
from user.permissions import IsAdminOrSelfOrAuthenticated 
from utils.auto_swagger import auto_swagger
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema


@auto_swagger(UserRequestSerializer, UserResponseSerializer)
class UserViewset(viewsets.ModelViewSet):
    """ CRUD para usuarios. """
    queryset = User.objects.all()
    serializer_class = UserRequestSerializer
    permission_classes = [IsAdminOrSelfOrAuthenticated]


    @swagger_auto_schema(responses={200: UserResponseSerializer})
    @action(detail=False, methods=['get'], url_path='me')
    def me(self, request):
        """ Retorna os dados do usuário autenticado """
        serializer = UserResponseSerializer(request.user)
        return Response(serializer.data)

