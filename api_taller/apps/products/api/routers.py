from django.urls import path,include
from rest_framework.routers import DefaultRouter
from apps.products.api.api import ProductViewSet,BuysProductViewSet,SellProductViewSet,DiscountsViewSet,SellProductStatisticsViewSet

router= DefaultRouter()
router.register(r'products',ProductViewSet, basename="products")
router.register(r'add_buy_product',BuysProductViewSet, basename="add_buy_product")
router.register(r'add_sell_product',SellProductViewSet, basename="add_sell_product")
router.register(r'discounts',DiscountsViewSet, basename="discounts")
router.register(r'statistics_sell_products',SellProductStatisticsViewSet, basename="statistics_sell_products")


urlpatterns = [
    path('', include(router.urls)),
]