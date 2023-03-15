from rest_framework import serializers
from apps.employee.models import Employees, Employees_type
from apps.customer.api.serializers import DocumentTypeSerializers

class EmployeesTypeSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=Employees_type
        fields='__all__'
        

class EmployeesSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=Employees
        fields='__all__'
        
class GetEmployeesTypeSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=Employees
        fields='__all__'
        
    employees_type_id=EmployeesTypeSerializers(
        many=False,
        read_only=True,
    )
    
    documents_type=DocumentTypeSerializers(
        many=False,
        read_only=True,
    )
        


