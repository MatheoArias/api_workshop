from rest_framework import viewsets
from apps.employee.models import Employees, Employees_type
from apps.employee.api.serializers import EmployeesSerializers, EmployeesTypeSerializers

class EmployeesViewSet(viewsets.ModelViewSet):
    serializer_class=EmployeesSerializers
    queryset=Employees.objects.all()

class EmployeesTypeViewSet(viewsets.ModelViewSet):
    serializer_class=EmployeesTypeSerializers
    queryset=Employees_type.objects.all()
