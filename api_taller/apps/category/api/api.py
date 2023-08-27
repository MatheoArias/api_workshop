from rest_framework import viewsets
from apps.category.api.serializers import ProductCategoriesSerilaizers
from apps.category.models import ProductCategories

class ProductCategoriesViewSet(viewsets.ModelViewSet):
    serializer_class=ProductCategoriesSerilaizers
    queryset=ProductCategories.objects.all()
    
