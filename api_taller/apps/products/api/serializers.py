from rest_framework import serializers
from apps.products.models import Products, Buys_products,Sell_products,Discounts
from apps.category.api.serializers import ProductCategoriesSerilaizers
from django.db.models import Avg, Max, Min,Sum,Count
from datetime import datetime
from statistics import median
import math



class GetCategoriesSerializer(serializers.ModelSerializer):
    
    category_id = ProductCategoriesSerilaizers(
        many=False,
        read_only=True,
    )
    
    class Meta:
        model = Products
        fields = '__all__'
    
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

    total_buys=serializers.SerializerMethodField()
    class Meta:

        model = Buys_products
        fields = 'id','product_id','buys_date','buys_bill','buys_stock','buys_unit_value','tax_buy','total_buys'
    
    def get_total_buys(self,obj):
        buy_product=Buys_products.objects.get(pk=obj.pk)
        tax_buy=buy_product.tax_buy + 1
        price_base=buy_product.buys_unit_value/tax_buy
        subtotal=price_base * buy_product.buys_stock
        tax_value=subtotal*buy_product.tax_buy
        total_buy=subtotal+tax_value
        return {'price_base_buy':price_base,'subtotal':subtotal,'tax':tax_value,'total':total_buy}
    
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
    
    total_sell=serializers.SerializerMethodField()
    class Meta:

        model = Sell_products
        fields = 'id','product_id','sell_date','sell_bill','sell_stock','tax_sell','discount_id','total_sell'
            
    def get_total_sell(self,obj):
        sell_product=Sell_products.objects.get(pk=obj.pk)
        product=Products.objects.get(pk=sell_product.product_id.id)
        
        unit_sell_value=product.unit_value + (product.percentage * product.unit_value)
        stock=float(sell_product.sell_stock)
        subtotal =unit_sell_value * sell_product.sell_stock
        profit=product.percentage * product.unit_value  * stock
        tax_value=sell_product.tax_sell * float(subtotal)
        if sell_product.discount_id:
            percentage=float(sell_product.discount_id.percentage)
            discount=profit * percentage
        else:
            discount=0
        total=subtotal- discount + tax_value
        return {'subtotal':subtotal,'tax':tax_value,'discount':discount,'total':total}
                
class GetSellProductStatisticsSerializer(serializers.ModelSerializer):
    
    list_sell_stock = serializers.SerializerMethodField()
    
    year_sell_stock = serializers.SerializerMethodField()
    year_sum_sell_products = serializers.SerializerMethodField()
    
    month_sell_stock = serializers.SerializerMethodField()
    month_sum_sell_products = serializers.SerializerMethodField()
    month_median_sell_products=serializers.SerializerMethodField()
    
    day_sell_stock = serializers.SerializerMethodField()
    day_sum_sell_products = serializers.SerializerMethodField()
    
    class Meta:

        model = Sell_products
        fields = 'id','product_id','sell_date','sell_bill','sell_stock','discount_id','list_sell_stock', 'year_sell_stock','year_sum_sell_products','month_sell_stock','month_sum_sell_products','month_median_sell_products','day_sell_stock','day_sum_sell_products'
    
    
    #This is product more sell
    def get_list_sell_stock(self, obj):
        return Sell_products.objects.values('product_id').annotate(Count('sell_stock'))
    
    ##For year
    #This is products sell year
    def get_year_sell_stock(self,obj):
        return Sell_products.objects.values('sell_date__year').annotate(Count('sell_stock'))
    
    def get_year_sum_sell_products(self,obj):
        dt = datetime.now()
        return Sell_products.objects.values('sell_date__year').annotate(Sum('product_id__unit_value'))
    
    ##For Month
    #This is products sell month        
    def get_month_sell_stock(self,obj):
        return Sell_products.objects.values('sell_date__month').annotate(Count('sell_stock'))
    
    def get_month_sum_sell_products(self,obj):
        return Sell_products.objects.values('sell_date__month').annotate(Sum('product_id__unit_value'))
    
    def get_month_median_sell_products(self,obj):
        queryset= Sell_products.objects.values('sell_date__month').annotate(Sum('product_id__unit_value')).values_list('product_id__unit_value__sum')
        return median(queryset)
    
    
    #This is products sell day in the month
    def get_day_sell_stock(self,obj):
        dt = datetime.now()
        return Sell_products.objects.filter(sell_date__month=dt.month).values('sell_date').annotate(Count('sell_stock'))
        d
    def get_day_sum_sell_products(self,obj):
        dt = datetime.now()
        return Sell_products.objects.filter(sell_date__month=dt.month).values('sell_date').annotate(Sum('product_id__unit_value'))
    