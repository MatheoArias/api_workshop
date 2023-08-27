from django.db import models
from apps.category.models import ProductCategories


class Products(models.Model):
    code=models.CharField("Codigo", max_length=50, unique=True,blank=False, null=False)
    description=models.CharField("Descripcion", max_length=200, blank=False, null=False)
    category_id=models.ForeignKey(ProductCategories, verbose_name="Categoria", on_delete=models.CASCADE)
    total_stock=models.IntegerField('Existencias', blank=False,null=False)
    
    verbose_name = "Producto"
    verbose_name_plural = "Productos"
    ordering = ["code"]


    def __str__(self):
        return f'{self.code} - {self.description}'


class Buys_products(models.Model):
    product_id=models.ForeignKey(Products, verbose_name="Producto", on_delete=models.CASCADE)
    buys_date=models.DateField("Fecha de compra", auto_now=False, auto_now_add=False)
    buys_bill=models.CharField("Factura de compra", max_length=100, unique=False, blank=False,null=False)
    buys_stock=models.IntegerField("Cantidad de entrada")
    buys_unit_value=models.FloatField("Valor unidad")
    tax_buy=models.FloatField("I.V.A", null=True)

    
    verbose_name = "Producto de entrada"
    verbose_name_plural = "Productos de entrada"
    ordering = ["product_id"]

    def __str__(self):
        return f'{self.product_id}'

class Discounts(models.Model):
    types=models.CharField("Tipo", max_length=100,blank=False, null=False)
    description=models.CharField("Descripción", max_length=250,blank=False, null=False)
    percentage=models.DecimalField("Porcentaje", max_digits=10, decimal_places=2)
    
    verbose_name = "Descuento"
    verbose_name_plural = "Descuentos"
    ordering = ["types"]
    
    def __str__(self):
        return f'{self.types} - {self.description}- {self.percentage}'

class Sell_products(models.Model):
    
    product_id=models.ForeignKey(Products, verbose_name="Producto", on_delete=models.CASCADE)
    sell_date=models.DateField("Fecha de venta", auto_now=False, auto_now_add=False)
    sell_bill=models.CharField("Factura de venta", max_length=100, unique=False, blank=False,null=False)
    sell_stock=models.IntegerField("Cantidad de Salida")
    discount_id=models.ForeignKey(Discounts,verbose_name="Descuento", on_delete=models.CASCADE,null=True)
    tax_sell=models.FloatField("I.V.A", null=True)

    verbose_name = "Producto de Salida"
    verbose_name_plural = "Productos de Salida"
    ordering = ["product_id"]

    def __str__(self):
        return f'{self.product_id}'
