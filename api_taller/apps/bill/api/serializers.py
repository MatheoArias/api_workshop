from rest_framework import serializers
from apps.bill.models import Discounts,PaymentMedium,Bill
from apps.vehicle.api.serializers import VehicleSerilaizers
from apps.customer.api.serializers import CustomerSerilizers,GetDocumentTypeSerializers
from apps.employee.api.serializers import GetEmployeesTypeSerializers
from apps.products.api.serializers import GetSellProductSerilaizers

class DiscountsSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=Discounts
        fields='__all__'

            
class PaymentMediumSerilizers(serializers.ModelSerializer):
    
    class Meta:
        model=PaymentMedium
        fields='__all__' 
          
class BillSerializers(serializers.ModelSerializer):

    class Meta:
        model=Bill
        fields='__all__'
        
class GetModelsSerializers(serializers.ModelSerializer):

    class Meta:
        model=Bill
        fields='__all__'
    
    employee_id = GetEmployeesTypeSerializers(
        many=False,
        read_only=True,
    )
    
    discounts_id= DiscountsSerializers(
        many=False,
        read_only=True,
    )

    customer_id=GetDocumentTypeSerializers(
        many=False,
        read_only=True,
    )
    
    vehicle_id=VehicleSerilaizers(
        many=False,
        read_only=True,  
    )
    
    payment_medium_id=PaymentMediumSerilizers(
        many=False,
        read_only=True, 
    )
    
    products_sell=GetSellProductSerilaizers(
        many=True,
        read_only=False, 
    )
