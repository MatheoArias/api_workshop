from django.db import models

class Categories(models.Model):
    category=models.CharField("Categoría", unique=True, null=False, max_length=50, blank=False)
    
    verbose_name = "Categoría"
    verbose_name_plural = "Categorías"
    ordering = ["category"]
    
    def __str__(self):
        return self.category
    
    