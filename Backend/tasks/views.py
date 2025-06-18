from rest_framework import viewsets

from users.permissions import IsAdminOrSelfOrAuthenticated 
from tasks.models import Task
from tasks.serializers import TaskSerializer

class TaskViewset(viewsets.ModelViewSet):
    "CRUD de tarefas"
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAdminOrSelfOrAuthenticated]
