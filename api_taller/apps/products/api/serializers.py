from rest_framework import serializers
from apps.products.models import Products, Buys_products,Sell_products,Discounts
from apps.category.api.serializers import CategoriesSerilaizers



class GetCategoriesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Products
        fields = '__all__'
    
    category_id = CategoriesSerilaizers(
        many=False,
        read_only=True,
    )   

class DiscountsSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=Discounts
        fields='__all__'


class ProductSerilaizers(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'


class BuysProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Buys_products
        fields = '__all__'


class GetBuyProductSerilaizers(serializers.ModelSerializer):
    
    product_id = GetCategoriesSerializer(
        many=False,
        read_only=True,
    )

    class Meta:

        model = Buys_products
        fields = '__all__'      


class SellProductsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sell_products
        fields = '__all__'

  
class GetSellProductSerilaizers(serializers.ModelSerializer):
    
    product_id = GetCategoriesSerializer(
        many=False,
        read_only=True,
    )
    
    discount_id=DiscountsSerializers(
        many=False,
        read_only=True,
    )

    class Meta:

        model = Sell_products
        fields = '__all__'  
