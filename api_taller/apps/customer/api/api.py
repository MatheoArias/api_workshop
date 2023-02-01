from rest_framework import viewsets
from apps.customer.api.serializers import CustomerSerilizers
from apps.customer.models import Customer


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class=CustomerSerilizers
    queryset=Customer.objects.all()