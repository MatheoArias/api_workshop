from django.db import models
from apps.products.models import Sell_products
from apps.customer.models import Customer
from apps.vehicle.models import Vehicle
from apps.employee.models import Employees

class PaymentMedium(models.Model):
    medium=models.CharField("Medio de pago", max_length=50,blank=False,null=False,unique=True)
    
    verbose_name = "Método Pago"
    verbose_name_plural = "Métodos de Pago"
    ordering = ["medium"]
    
    def __str__(self):
        return f'{self.medium}'


class Bill(models.Model):
    """Change null=False"""
    customer= models.ForeignKey(Customer, verbose_name="Cliente",blank=False, null=True, on_delete=models.CASCADE)
    vehicle= models.ForeignKey(Vehicle, verbose_name="Vehículo",blank=True, null=True, on_delete=models.CASCADE)
    employee=models.ForeignKey(Employees, verbose_name="Empleado",blank=True, null=True, on_delete=models.CASCADE)
    payment_medium=models.ForeignKey(PaymentMedium, verbose_name="Medio de pago", on_delete=models.CASCADE,null=True)
    products_sell=models.ManyToManyField(Sell_products, verbose_name="Productos")
    subtotal=models.DecimalField("Subtotal", max_digits=10, decimal_places=2)
    tax=models.DecimalField("I.V.A.", max_digits=10, decimal_places=2, default=0.19)
    tax_surcharge=models.DecimalField("Recargo", max_digits=10, decimal_places=2,null=True)                                          
    total_value=models.DecimalField("Valor total", max_digits=10, decimal_places=2)
    
    verbose_name = "Factura"
    verbose_name_plural = "Facturas"
    ordering = ["id"]
    
    
    def __str__(self):
        return f'{self.id}'