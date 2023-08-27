from rest_framework import serializers
from apps.vehicle.models import Vehicle
from apps.category.api.serializers import ProductCategoriesSerilaizers
from apps.customer.api.serializers import GetDocumentTypeSerializers


class VehicleSerilaizers(serializers.ModelSerializer):
    
    class Meta:
        model=Vehicle
        fields='__all__'
    

class GetModelsSerializers(serializers.ModelSerializer):

    class Meta:
        model=Vehicle
        fields='__all__'
     
    category= ProductCategoriesSerilaizers(
        many=False,
        read_only=True,
    )
    
    owner=GetDocumentTypeSerializers(
        many=False,
        read_only=True,
    )
                    
