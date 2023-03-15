from rest_framework import viewsets
from apps.vehicle.api.serializers import VehicleSerilaizers,GetModelsSerializers
from apps.vehicle.models import Vehicle

class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class=VehicleSerilaizers
    queryset=Vehicle.objects.all()

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.action == 'list' or self.action == 'retrieve':
            serializer_class = GetModelsSerializers
        return serializer_class