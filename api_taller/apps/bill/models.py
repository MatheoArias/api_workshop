from django.db import models
from apps.products.models import Sell_products
from apps.customer.models import Customer
from apps.vehicle.models import Vehicle
from apps.employee.models import Employees


class Discounts(models.Model):
    types=models.CharField("Tipo", max_length=20,blank=False, null=False)
    description=models.CharField("Descripción", max_length=250,blank=False, null=False)
    percentage=models.DecimalField("Porcentaje", max_digits=10, decimal_places=2)
    
    verbose_name = "Descuento"
    verbose_name_plural = "Descuentos"
    ordering = ["types"]
    
    def __str__(self):
        return f'{self.types} - {self.description}- {self.percentage}'
    

class PaymentMedium(models.Model):
    medium=models.CharField("Medio de pago", max_length=50,blank=False,null=False,unique=True)
    
    verbose_name = "Método Pago"
    verbose_name_plural = "Métodos de Pago"
    ordering = ["medium"]
    
    def __str__(self):
        return f'{self.medium}'


class Bill(models.Model):
    """Change null=False"""
    customer_id = models.ForeignKey(Customer, verbose_name="Cliente",blank=False, null=False, on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey(Vehicle, verbose_name="Vehículo",blank=True, null=True, on_delete=models.CASCADE)
    employee_id=models.ForeignKey(Employees, verbose_name="Empleado",blank=True, null=True, on_delete=models.CASCADE)
    payment_medium_id=models.ForeignKey(PaymentMedium, verbose_name="Medio de pago", on_delete=models.CASCADE,null=True)
    products_sell=models.ManyToManyField(Sell_products, verbose_name="Productos")
    discounts_id=models.ForeignKey(Discounts, verbose_name="Descuento", on_delete=models.CASCADE, null=True)
    discount_value=models.DecimalField("Monto de descuento", max_digits=10, decimal_places=2,null=True)  
    subtotal=models.DecimalField("Subtotal", max_digits=10, decimal_places=2)
    tax=models.DecimalField("I.V.A.", max_digits=10, decimal_places=2, default=0.19)
    tax_surcharge=models.DecimalField("Recargo", max_digits=10, decimal_places=2,null=True)                                          
    total_value=models.DecimalField("Valor total", max_digits=10, decimal_places=2)
    
    verbose_name = "Factura"
    verbose_name_plural = "Facturas"
    ordering = ["id"]
    
    
    def __str__(self):
        return f'{self.id}'