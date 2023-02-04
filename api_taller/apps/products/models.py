from django.db import models
from apps.vehicle.models import Categories


"""This is the class of products:
Example:
    code: "M000001",
    description: "Farola-GS125",
    totals_stock": 50,
    category_id: 1
"""
class Products(models.Model):
    code=models.CharField("Código", max_length=50, unique=True,blank=False, null=False)
    description=models.CharField("Descripción", max_length=200)
    category_id=models.ForeignKey(Categories, verbose_name="Categoría", on_delete=models.CASCADE)
    unit_value=models.IntegerField("Valor unitario")
    totals_stock=models.IntegerField('Inventario total')
    
    verbose_name = "Producto"
    verbose_name_plural = "Productos"
    ordering = ["code"]


    def __str__(self):
        return f'{self.code} - {self.description}'

"""This is Buy's Bill // Estos son los productos de Compra
Example: 

    product_id: {
        category_id: {
            category: "Moto"
        },
        code: "M000001",
        description: "Farola-GS125",
        unit_value: 10000,
        totals_stock: 50
    },
    buys_date: "2023-02-04",
    buys_bill: "FC00001",
    buys_stock: 12,
    buys_unit_value: 9500,
    total_buys_value" 114000

"""
class Buys_products(models.Model):
    product_id=models.ForeignKey(Products, verbose_name="Producto", on_delete=models.CASCADE)
    buys_date=models.DateField("Fecha de compra", auto_now=False, auto_now_add=False)
    buys_bill=models.CharField("Factura de compra", max_length=100, unique=True, blank=False,null=False)
    buys_stock=models.IntegerField("Cantidad de entrada")
    buys_unit_value=models.DecimalField("Valor unidad", max_digits=11, decimal_places=2)
    total_buys_value=models.DecimalField("Total", max_digits=11, decimal_places=2)
    
    
    verbose_name = "Producto de entrada"
    verbose_name_plural = "Productos de entrada"
    ordering = ["product_id"]

    def __str__(self):
        return f'{self.product_id}'



class Sell_products(models.Model):
    
    product_id=models.ForeignKey(Products, verbose_name="Producto", on_delete=models.CASCADE)
    sell_date=models.DateField("Fecha de venta", auto_now=False, auto_now_add=False)
    sell_bill=models.CharField("Factura de venta", max_length=100, unique=True, blank=False,null=False)
    sell_stock=models.IntegerField("Cantidad de Salida")
    total_sell_value=models.DecimalField("Total", max_digits=11, decimal_places=2)
    
    
    verbose_name = "Producto de Salida"
    verbose_name_plural = "Productos de Salida"
    ordering = ["product_id"]

    def __str__(self):
        return f'{self.product_id}'
