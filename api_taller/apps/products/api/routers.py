from django.urls import path,include
from rest_framework.routers import DefaultRouter
from apps.products.api.api import ProductViewSet,BuysProductViewSet

router= DefaultRouter()

router.register(r'add_product',ProductViewSet, basename="add_product")
router.register(r'add_product_inputs',BuysProductViewSet, basename="add_product_inputs")

urlpatterns = [
    path('', include(router.urls)),
]