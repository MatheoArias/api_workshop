from rest_framework import serializers
from apps.products.models import Products, Buys_products,Sell_products,Discounts
from apps.category.api.serializers import CategoriesSerilaizers
from django.db.models import Avg, Max, Min,Sum,Count
from datetime import datetime
from statistics import median



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

class GetSellProductStatisticsSerializer(serializers.ModelSerializer):
    
    list_sell_stock = serializers.SerializerMethodField()
    
    year_sell_stock = serializers.SerializerMethodField()
    year_sum_sell_products = serializers.SerializerMethodField()
    
    month_sell_stock = serializers.SerializerMethodField()
    month_sum_sell_products = serializers.SerializerMethodField()
    month_median_sell_products=serializers.SerializerMethodField()
    
    day_sell_stock = serializers.SerializerMethodField()
    day_sum_sell_products = serializers.SerializerMethodField()
    day_median_sell_products=serializers.SerializerMethodField()
    
    class Meta:

        model = Sell_products
        fields = 'id','product_id','sell_date','sell_bill','sell_stock','discount_id','list_sell_stock', 'year_sell_stock','year_sum_sell_products','month_sell_stock','month_sum_sell_products','month_median_sell_products','day_sell_stock','day_sum_sell_products','day_median_sell_products'
    
    
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
        
    def get_day_sum_sell_products(self,obj):
        dt = datetime.now()
        return Sell_products.objects.filter(sell_date__month=dt.month).values('sell_date').annotate(Sum('product_id__unit_value'))
    
    
    def get_day_median_sell_products(self,obj):
        dt = datetime.now()
        queryset=Sell_products.objects.filter(sell_date__month=dt.month).values('sell_date').annotate(Sum('product_id__unit_value')).values_list('product_id__unit_value__sum')
        return median(queryset) 
    