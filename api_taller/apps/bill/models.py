from django.db import models
from apps.products.models import Products
from apps.customer.models import Customer
from apps.vehicle.models import Vehicle


'''This class is:
    product_id: this is the code of product created un apps.products
    Cuantity: this is the cuantity in stock of products
    total_Value:'''
class Bill_product(models.Model):
    product_id = models.ForeignKey(Products, verbose_name="Item", on_delete=models.CASCADE)
    cuantity = models.IntegerField("Cantidad", default=0)
    total_value=models.DecimalField("valor total", max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = "Producto de factura"
        verbose_name_plural = "Producto de facturas"
        ordering = ["product_id"]
    
    
    def __str__(self):
        return f'{self.product_id}'


class Bill(models.Model):
    date_time_bill=models.DateTimeField("Fecha y Hora", auto_now_add=True)
    customer_id = models.ForeignKey(Customer, verbose_name="Cliente",blank=False, null=False, on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey(Vehicle, verbose_name="Vehículo",blank=True, null=True, on_delete=models.CASCADE)
    city_bill=models.CharField("Ciudad", max_length=100,blank=False, null=False)
    payments_method=models.CharField("Método de pago", max_length=20,blank=False, null=False)
    payments_medium=models.CharField("Medio de pago", max_length=20,blank=False, null=False)
    products_bill_id=models.ManyToManyField(Bill_product, verbose_name="Productos")
    subtotal=models.DecimalField("Subtotal", max_digits=10, decimal_places=2)
    iva=models.DecimalField("I.V.A.", max_digits=10, decimal_places=2)
    total_value=models.DecimalField("valor total", max_digits=10, decimal_places=2)
    
    
    verbose_name = "Factura"
    verbose_name_plural = "Facturas"
    ordering = ["id"]
    
    
    def __str__(self):
        return f'{self.id}'
    