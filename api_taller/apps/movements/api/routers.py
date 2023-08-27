from django.urls import path,include
from rest_framework.routers import DefaultRouter
from apps.movements.api.api import InputProductViewSet, OutputProductViewSet

router= DefaultRouter()
router.register(r'input_product',InputProductViewSet, basename="input_product")
router.register(r'output_product',OutputProductViewSet, basename="output_product")


urlpatterns = [
    path('', include(router.urls)),
]