from django.urls import path, include
from .views import TagViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tag', TagViewset, basename='tags')

urlpatterns = [
    path('', include(router.urls)),
]