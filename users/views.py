from rest_framework import viewsets
from django.contrib.auth.models import User
from users.serializers import UserRequestSerializer, UserResponseSerializer
from users.permissions import IsAdminOrSelfOrAuthenticated 
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema


class UserViewset(viewsets.ModelViewSet):
    """ CRUD para usuarios. """
    queryset = User.objects.all()
    serializer_class = UserRequestSerializer
    permission_classes = [IsAdminOrSelfOrAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return UserRequestSerializer
        return UserResponseSerializer

    @swagger_auto_schema(
            request_body=UserRequestSerializer,
            responses={200: UserResponseSerializer})
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
            request_body=UserRequestSerializer,
            responses={200: UserResponseSerializer})
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(responses={200: UserResponseSerializer})
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
            request_body=UserRequestSerializer,
            responses={200: UserResponseSerializer})
    def partial_update(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
        
    @swagger_auto_schema(responses={200: UserResponseSerializer})
    @action(detail=False, methods=['get'], url_path='me')
    def me(self, request):
        """ Retorna os dados do usuário autenticado """
        serializer = UserResponseSerializer(request.user)
        return Response(serializer.data)

