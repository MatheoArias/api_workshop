from django.urls import path,include
from rest_framework.routers import DefaultRouter
from apps.vehicle.api.api import VehicleViewSet

router= DefaultRouter()

router.register(r'add_vehicle',VehicleViewSet, basename="add_vehicle")

urlpatterns = [
    path('', include(router.urls)),
]