from rest_framework import serializers
from apps.products.models import Products, Buys_products,Sell_products,Discounts
from apps.category.api.serializers import CategoriesSerilaizers
from django.db.models import Avg, Max, Min,Sum,Count
from datetime import datetime
from statistics import median
import math



class GetCategoriesSerializer(serializers.ModelSerializer):
    
    category_id = CategoriesSerilaizers(
        many=False,
        read_only=True,
    )
    
    buy_value=serializers.SerializerMethodField()
    sell_value=serializers.SerializerMethodField()
    profit=serializers.SerializerMethodField()
    
    class Meta:
        model = Products
        fields = 'id','category_id','description','code','unit_value','percentage','profit','last_tax_buy','totals_stock','buy_value','sell_value'
    
    ##This function id for add products profit
    def get_profit(self,obj):
        product=Products.objects.get(pk=obj.pk)
        unit_value=product.unit_value
        profit=math.ceil((product.percentage * unit_value)/100)*100
        return profit
    
    ##This function is for add products's buy price
    def get_buy_value(self,obj):
        product=Products.objects.get(pk=obj.pk)
        last_tax_buy=product.last_tax_buy + 1
        unit_value=product.unit_value
        return math.floor(unit_value/last_tax_buy)

    ##This function is for add products's sell price
    def get_sell_value(self,obj):
        product=Products.objects.get(pk=obj.pk)
        last_tax_buy=product.last_tax_buy
        unit_value=product.unit_value
        sell_subprice=unit_value + (product.percentage * unit_value)
        subtotal=math.floor(sell_subprice/100)*100
        tax=math.ceil((subtotal * last_tax_buy)/100)*100
        total=subtotal + tax
        return {'subtotal_sell':subtotal,'tax':tax,'total_sell':total} 
        
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

    price_base_buy=serializers.SerializerMethodField()
    class Meta:

        model = Buys_products
        fields = 'tax_buy','id','product_id','buys_date','buys_bill','buys_stock','buys_unit_value','price_base_buy'
    
    def get_price_base_buy(self,obj):
        buy_product=Buys_products.objects.get(pk=obj.pk)
        product=Products.objects.get(pk=buy_product.product_id.id)
        tax_buy=buy_product.tax_buy + 1
        price_base=math.floor(product.unit_value/tax_buy)
        return {'price_base':price_base,'tax_buy':product.unit_value-price_base}
    
    
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
        fields = 'tax_sell','id','product_id','sell_date','sell_bill','sell_stock','discount_id','total_sell'
            
    def get_total_sell(self,obj):
        sell_product=Sell_products.objects.get(pk=obj.pk)
        product=Products.objects.get(pk=sell_product.product_id.id)
        sell_unit=math.floor((product.unit_value + (product.percentage * product.unit_value))/100)*100
        subtotal =math.ceil(sell_unit * sell_product.sell_stock)
        profit=(math.ceil((product.percentage * product.unit_value)/100)*100) * sell_product.sell_stock
        tax_value=math.ceil((sell_product.tax_sell * subtotal)/100)*100
        if sell_product.discount_id:
            discount= math.ceil((profit * sell_product.discount_id.percentage)/100)*100
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
    