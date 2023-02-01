from rest_framework import serializers
from apps.employee.models import Employees, Employees_type

class EmployeesSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=Employees
        fields='__all__'
        
    employees_type_id=serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='jobs_names'
    )    


class EmployeesTypeSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=Employees_type
        fields='__all__'