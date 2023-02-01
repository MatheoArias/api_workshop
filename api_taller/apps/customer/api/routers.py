from django.urls import path,include
from rest_framework.routers import DefaultRouter
from apps.customer.api.api import CustomerViewSet

router= DefaultRouter()

router.register(r'addcustomer',CustomerViewSet, basename="addcustomer")

urlpatterns = [
    path('', include(router.urls)),
]