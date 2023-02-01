from rest_framework import viewsets
from apps.vehicle.api.serializers import VehicleSerilaizers
from apps.vehicle.models import Vehicle

class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class=VehicleSerilaizers
    queryset=Vehicle.objects.all()
