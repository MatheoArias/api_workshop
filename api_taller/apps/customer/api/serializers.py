from rest_framework import serializers
from apps.customer.models import Customer,DocumentType


class DocumentTypeSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=DocumentType
        fields='__all__'
    
class CustomerSerilizers(serializers.ModelSerializer):
    
    class Meta:
        model=Customer
        fields='__all__'

class GetDocumentTypeSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=Customer
        fields='__all__'

    document_type = DocumentTypeSerializers(
        many=False,
        read_only=True,
    )