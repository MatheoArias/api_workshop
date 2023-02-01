from django.urls import path,include
from rest_framework.routers import DefaultRouter
from apps.category.api.api import CategoriesViewSet

router= DefaultRouter()

router.register(r'add_category',CategoriesViewSet, basename="add_category")

urlpatterns = [
    path('', include(router.urls)),
]