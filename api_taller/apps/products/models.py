from django.db import models
from apps.vehicle.models import Categories

class Products(models.Model):
    code=models.CharField("Código", max_length=50, unique=True,blank=False, null=False)
    description=models.CharField("Descripción", max_length=200)
    category_id=models.ForeignKey(Categories, verbose_name="Categoría", on_delete=models.CASCADE)
    totals_stock=models.IntegerField('Inventario total')
    
    verbose_name = "Producto"
    verbose_name_plural = "Productos"
    ordering = ["code"]


    def __str__(self):
        return f'{self.code}'

class Buys_products(models.Model):
    product_id=models.ForeignKey(Products, verbose_name="Código Producto", on_delete=models.CASCADE)
    buys_date=models.DateField("Fecha de compra", auto_now=False, auto_now_add=False)
    buys_bill=models.CharField("Factura de compra", max_length=100, unique=True, blank=False,null=False)
    buys_stock=models.IntegerField("Cantidad de entrada")
    
    verbose_name = "Producto de entrada"
    verbose_name_plural = "Productos de entrada"
    ordering = ["product_id"]

    def __str__(self):
        return f'{self.product_id}'
