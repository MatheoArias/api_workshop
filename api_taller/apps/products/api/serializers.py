from rest_framework import serializers
from apps.products.models import Products,Buys_products
from apps.category.api.serializers import CategoriesSerilaizers
   
class ProductSerilaizers(serializers.ModelSerializer):
    
    class Meta:
        model=Products
        fields='__all__'


class GetVehicleTypeSerilaizers(serializers.ModelSerializer):
    
    product_category_id=CategoriesSerilaizers(
        many=False,
        read_only=True,
    )
    
    class Meta:
        model=Products
        fields='__all__'


class BuysProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Buys_products
        fields='__all__'
    
  
class GetProductSerilaizers(serializers.ModelSerializer):
    
    product_id=ProductSerilaizers(
        many=False,
        read_only=True,
    )
    
    class Meta:
        
        model=Buys_products
        fields='__all__'



