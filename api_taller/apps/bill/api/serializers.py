from rest_framework import serializers
from apps.bill.models import PaymentMedium,Bill
from apps.vehicle.api.serializers import VehicleSerilaizers
from apps.customer.api.serializers import CustomerSerilizers,GetDocumentTypeSerializers
from apps.employee.api.serializers import GetEmployeesTypeSerializers
from apps.products.api.serializers import GetSellProductSerilaizers
     
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
    
    employee = GetEmployeesTypeSerializers(
        many=False,
        read_only=True,
    )
    
    customer = GetDocumentTypeSerializers(
        many=False,
        read_only=True,
    )
    
    vehicle = VehicleSerilaizers(
        many=False,
        read_only=True,  
    )
    
    payment_medium = PaymentMediumSerilizers(
        many=False,
        read_only=True, 
    )
    
    products_sell=GetSellProductSerilaizers(
        many=True,
        read_only=False, 
    )
