from rest_framework import viewsets
from apps.category.api.serializers import CategoriesSerilaizers
from apps.vehicle.models import Categories

class CategoriesViewSet(viewsets.ModelViewSet):
    serializer_class=CategoriesSerilaizers
    queryset=Categories.objects.all()
    
