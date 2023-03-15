from rest_framework import viewsets
from apps.employee.models import Employees, Employees_type
from apps.employee.api.serializers import EmployeesSerializers, EmployeesTypeSerializers,GetEmployeesTypeSerializers

class EmployeesTypeViewSet(viewsets.ModelViewSet):
    serializer_class=EmployeesTypeSerializers
    queryset=Employees_type.objects.all()


class EmployeesViewSet(viewsets.ModelViewSet):
    serializer_class=EmployeesSerializers
    queryset=Employees.objects.all()
    
    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.action == 'list' or self.action == 'retrieve':
            serializer_class = GetEmployeesTypeSerializers
        return serializer_class

