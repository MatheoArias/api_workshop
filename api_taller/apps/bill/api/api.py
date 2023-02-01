from rest_framework import viewsets
from apps.bill.api.serializers import BillSerializers, BillProductSerializers
from apps.bill.models import Bill,Bill_product

class BillViewSet(viewsets.ModelViewSet):
    serializer_class=BillSerializers
    queryset=Bill.objects.all()

class BillProducteViewSet(viewsets.ModelViewSet):
    serializer_class=BillProductSerializers
    queryset=Bill_product.objects.all()
    

