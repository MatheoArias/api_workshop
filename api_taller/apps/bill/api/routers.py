from django.urls import path,include
from rest_framework.routers import DefaultRouter
from apps.bill.api.api import  BillViewSet,DiscountsViewSet,PaymentMediumViewSet

router= DefaultRouter()

router.register(r'add_bill',BillViewSet, basename="add_bill")
router.register(r'discounts',DiscountsViewSet, basename="discounts")
router.register(r'payment_medium',PaymentMediumViewSet, basename="payment_medium")

urlpatterns = [
    path('', include(router.urls)),
]