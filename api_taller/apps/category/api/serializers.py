from rest_framework import serializers
from apps.category.models import ProductCategories

"""I convert since the DB to the JSON object for the visualization of the information."""
class ProductCategoriesSerilaizers(serializers.ModelSerializer):
    
    class Meta:
        model=ProductCategories
        fields='__all__'
    
       