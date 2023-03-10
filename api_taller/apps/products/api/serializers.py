from rest_framework import serializers
from apps.products.models import Products, Buys_products,Sell_products
from apps.category.models import Categories
from apps.category.api.serializers import CategoriesSerilaizers


class ProductSerilaizers(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'

class ProductCategoriesSerilaizers(serializers.ModelSerializer):
    
    class Meta:
        model = Products
        fields = '__all__'
        
    category_id = CategoriesSerilaizers(
        many=False,
        read_only=True,
    )
    
    
class BuysProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Buys_products
        fields = '__all__'


class SellProductsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sell_products
        fields = '__all__'


class GetCategoriesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Products
        fields = '__all__'
    
    category_id = CategoriesSerilaizers(
        many=False,
        read_only=True,
    )

class GetBuyProductSerilaizers(serializers.ModelSerializer):
    
    product_id = ProductCategoriesSerilaizers(
        many=False,
        read_only=True,
    )

    class Meta:

        model = Buys_products
        fields = '__all__'        

class GetSellProductSerilaizers(serializers.ModelSerializer):
    
    product_id = ProductCategoriesSerilaizers(
        many=False,
        read_only=True,
    )

    class Meta:

        model = Sell_products
        fields = '__all__'  

