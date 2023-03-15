from django.urls import path,include
from rest_framework.routers import DefaultRouter
from apps.customer.api.api import CustomerViewSet,DocumenTypeViewSet

router= DefaultRouter()

router.register(r'add_customer',CustomerViewSet, basename="add_customer")
router.register(r'add_document_type',DocumenTypeViewSet, basename="add_document_type")

urlpatterns = [
    path('', include(router.urls)),
]