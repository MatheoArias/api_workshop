from rest_framework import serializers
from apps.customer.models import Customer

class CustomerSerilizers(serializers.ModelSerializer):
    
    class Meta:
        model=Customer
        fields='__all__'