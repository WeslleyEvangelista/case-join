from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TargetViewSet

router = DefaultRouter()
router.register(r'targets', TargetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]