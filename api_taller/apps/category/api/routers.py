from django.urls import path,include
from rest_framework.routers import DefaultRouter
from apps.category.api.api import ProductCategoriesViewSet

router= DefaultRouter()

"""The rout for go to to the information is product_category"""
router.register(r'product_category',ProductCategoriesViewSet, basename="product_category")

urlpatterns = [
    path('', include(router.urls)),
]