from django.db import models

"""
The app is make for speak spanish users
Categories:{
    id:1
    description: Tornillería
}
"""
class ProductCategories(models.Model):
    description=models.CharField("Descripcion", unique=True, null=False, max_length=50, blank=False)
    
    verbose_name = "Categoría"
    verbose_name_plural = "Categorías"
    ordering = ["descrption"]
    
    def __str__(self):
        return self.description
    
    