from rest_framework import serializers
from apps.vehicle.models import Vehicle


class VehicleSerilaizers(serializers.ModelSerializer):
    
    class Meta:
        model=Vehicle
        fields='__all__'
    
       
                    
