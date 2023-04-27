from rest_framework import viewsets
from rest_framework.response import Response
from apps.products.models import Products, Buys_products,Sell_products,Discounts
from apps.products.api.serializers import ProductSerilaizers, GetBuyProductSerilaizers, BuysProductSerializer,SellProductsSerializer,GetSellProductSerilaizers,GetCategoriesSerializer,DiscountsSerializers,GetSellProductStatisticsSerializer
from rest_framework.permissions import IsAuthenticated


class DiscountsViewSet(viewsets.ModelViewSet):
    serializer_class=DiscountsSerializers
    queryset=Discounts.objects.all()

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerilaizers
    queryset = Products.objects.all()
    
            
    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.action == 'list' or self.action == 'retreve':
            serializer_class =GetCategoriesSerializer
        return serializer_class


class BuysProductViewSet(viewsets.ModelViewSet):
    serializer_class = BuysProductSerializer
    queryset = Buys_products.objects.all()

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.action == 'list' or self.action == 'retrieve':
            serializer_class = GetBuyProductSerilaizers
        return serializer_class

 
class SellProductViewSet(viewsets.ModelViewSet):
    serializer_class = SellProductsSerializer
    queryset = Sell_products.objects.all()
    
    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.action == 'list' or self.action == 'retrieve':
            serializer_class = GetSellProductSerilaizers
        return serializer_class

 
class SellProductStatisticsViewSet(viewsets.ModelViewSet):
    serializer_class = SellProductsSerializer
    queryset = Sell_products.objects.all()
    
    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.action == 'list' or self.action == 'retrieve':
            serializer_class = GetSellProductStatisticsSerializer
        return serializer_class   


    
    
    
