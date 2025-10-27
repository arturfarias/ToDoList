from django.urls import path, include
from .views import TaskViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('task', TaskViewset, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
]