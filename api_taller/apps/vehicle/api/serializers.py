from rest_framework import serializers
from apps.vehicle.models import Vehicle
from apps.category.api.serializers import CategoriesSerilaizers
from apps.customer.api.serializers import GetDocumentTypeSerializers


class VehicleSerilaizers(serializers.ModelSerializer):
    
    class Meta:
        model=Vehicle
        fields='__all__'
    

class GetModelsSerializers(serializers.ModelSerializer):

    class Meta:
        model=Vehicle
        fields='__all__'
     
    category_id = CategoriesSerilaizers(
        many=False,
        read_only=True,
    )
    
    owner_id=GetDocumentTypeSerializers(
        many=False,
        read_only=True,
    )
                    
