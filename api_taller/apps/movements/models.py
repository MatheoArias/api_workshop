from django.db import models
from apps.products.models import Products

class Input_products(models.Model):
    product_id=models.ForeignKey(Products, verbose_name="Producto", on_delete=models.CASCADE)
    date=models.DateField("Fecha", auto_now=False, auto_now_add=False)
    total=models.IntegerField("Cantidad", blank=False, null=False)
    
    
    verbose_name = "Producto de entrada"
    verbose_name_plural = "Productos de entrada"
    ordering = ["product_id"]

    def __str__(self):
        return f'{self.product_id}'


class Output_products(models.Model):
    product_id=models.ForeignKey(Products, verbose_name="Producto", on_delete=models.CASCADE)
    date=models.DateField("Fecha", auto_now=False, auto_now_add=False)
    total=models.IntegerField("Cantidad", blank=False, null=False)
    
    verbose_name = "Producto de salida"
    verbose_name_plural = "Productos de salida"
    ordering = ["product_id"]

    def __str__(self):
        return f'{self.product_id}'