from rest_framework import viewsets
from apps.bill.api.serializers import BillSerializers,PaymentMediumSerilizers,GetModelsSerializers
from apps.bill.models import Bill,PaymentMedium



class PaymentMediumViewSet(viewsets.ModelViewSet):
    serializer_class=PaymentMediumSerilizers
    queryset=PaymentMedium.objects.all()

class BillViewSet(viewsets.ModelViewSet):
    serializer_class=BillSerializers
    queryset=Bill.objects.all()
    
    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.action == 'list' or self.action == 'retrieve':
            serializer_class =GetModelsSerializers
        return serializer_class
    