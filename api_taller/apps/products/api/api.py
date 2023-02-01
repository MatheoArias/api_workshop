from rest_framework import viewsets
from apps.products.models import Products,Buys_products
from apps.products.api.serializers import ProductSerilaizers,GetVehicleTypeSerilaizers,GetProductSerilaizers,BuysProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class=ProductSerilaizers
    queryset=Products.objects.all()
    
    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.action == 'list' or self.action == 'retrieve':
            serializer_class = GetVehicleTypeSerilaizers
        return serializer_class
    
class BuysProductViewSet(viewsets.ModelViewSet):
    serializer_class=BuysProductSerializer
    queryset=Buys_products.objects.all()
    
    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.action == 'list' or self.action == 'retrieve':
            serializer_class = GetProductSerilaizers
        return serializer_class
                

    


    
    
    
