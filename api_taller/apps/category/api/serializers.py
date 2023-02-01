from rest_framework import serializers
from apps.vehicle.models import Categories


class CategoriesSerilaizers(serializers.ModelSerializer):
    
    class Meta:
        model=Categories
        fields='__all__'
    
       