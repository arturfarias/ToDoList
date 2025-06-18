from rest_framework import viewsets
from .models import Tag
from .serializers import TagSerializer
from users.permissions import IsAdminOrSelfOrAuthenticated


class TagViewset(viewsets.ModelViewSet):
    """ CRUD de Tags. """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminOrSelfOrAuthenticated]
