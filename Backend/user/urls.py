from django.urls import path, include
from .views import UserViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', UserViewset, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]