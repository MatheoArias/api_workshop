from rest_framework import serializers
from apps.movements.models import Output_products, Input_products
from apps.category.api.serializers import ProductCategoriesSerilaizers
from apps.products.models import Products


class GetPorductCategoriesSerializer(serializers.ModelSerializer):
    
    category_id = ProductCategoriesSerilaizers(
        many=False,
        read_only=True,
    )
    
    class Meta:
        model = Products
        fields = '__all__'

class GetOutputProductSerializer(serializers.ModelSerializer):
    
    product_id = GetPorductCategoriesSerializer(
        many=False,
        read_only=True,
    )
    
    class Meta:
        model = Input_products
        fields = '__all__'
            
class OutputProductSerilaizers(serializers.ModelSerializer):
    
    class Meta:
        model = Output_products
        fields = '__all__'


class GetInputProductSerializer(serializers.ModelSerializer):
    
    product_id = GetPorductCategoriesSerializer(
        many=False,
        read_only=True,
    )
    
    class Meta:
        model = Input_products
        fields = '__all__'
        
class InputProductSerilaizers(serializers.ModelSerializer):
    
    class Meta:
        model = Input_products
        fields = '__all__'

