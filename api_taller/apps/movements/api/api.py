from rest_framework import viewsets
from apps.movements.models import Output_products,Input_products
from apps.movements.api.serializers import OutputProductSerilaizers, InputProductSerilaizers,GetInputProductSerializer,GetOutputProductSerializer
from rest_framework.permissions import IsAuthenticated

class OutputProductViewSet(viewsets.ModelViewSet):
    serializer_class=OutputProductSerilaizers
    queryset=Output_products.objects.all()
    
    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.action == 'list' or self.action == 'retreve':
            serializer_class =GetOutputProductSerializer
        return serializer_class
    
class InputProductViewSet(viewsets.ModelViewSet):
    serializer_class=InputProductSerilaizers
    queryset=Input_products.objects.all()
    
    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.action == 'list' or self.action == 'retreve':
            serializer_class =GetInputProductSerializer
        return serializer_class
    

