from rest_framework import serializers
from apps.bill.models import Bill,Bill_product
from apps.vehicle.api.serializers import VehicleSerilaizers
from apps.customer.api.serializers import CustomerSerilizers
from apps.products.api.serializers import ProductSerilaizers

class BillProductSerializers(serializers.ModelSerializer):
    
    product_id=ProductSerilaizers(
        many=False,
        read_only=True,
    )
    
    class Meta:
        model=Bill_product
        fields='__all__'
        
        
            
class BillSerializers(serializers.ModelSerializer):
    
    vehicle_id=VehicleSerilaizers(
        many=False,
        read_only=True,
    )
    
    customer_id=CustomerSerilizers(
        many=False,
        read_only=True,
    )
    
    products_bill_id=BillProductSerializers(
        many=True,
        read_only=True
    )
        
    class Meta:
        model=Bill
        fields='__all__'



    