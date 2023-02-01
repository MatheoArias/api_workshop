from django.urls import path,include
from rest_framework.routers import DefaultRouter
from apps.bill.api.api import BillProducteViewSet, BillViewSet

router= DefaultRouter()

router.register(r'addproductsbill',BillProducteViewSet, basename="addproductsbill")
router.register(r'addbill',BillViewSet, basename="addbill")

urlpatterns = [
    path('', include(router.urls)),
]