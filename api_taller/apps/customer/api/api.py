from rest_framework import viewsets
from apps.customer.api.serializers import CustomerSerilizers,DocumentTypeSerializers,GetDocumentTypeSerializers
from apps.customer.models import Customer,DocumentType


class DocumenTypeViewSet(viewsets.ModelViewSet):
    serializer_class=DocumentTypeSerializers
    queryset=DocumentType.objects.all()
    
class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class=CustomerSerilizers
    queryset=Customer.objects.all()
    
    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.action == 'list' or self.action == 'retrieve':
            serializer_class = GetDocumentTypeSerializers
        return serializer_class
