from django.urls import path,include
from rest_framework.routers import DefaultRouter
from apps.products.api.api import ProductViewSet,BuysProductViewSet,SellProductViewSet

router= DefaultRouter()

router.register(r'add_product',ProductViewSet, basename="add_product")
router.register(r'add_buy_product',BuysProductViewSet, basename="add_buy_product")
router.register(r'add_sell_product',SellProductViewSet, basename="add_sell_product")

urlpatterns = [
    path('', include(router.urls)),
]