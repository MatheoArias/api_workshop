from django.db import models
from apps.customer.models import Customer
from apps.category.models import Categories


class Vehicle(models.Model):
        license_plate=models.CharField("Placa", max_length=7,unique=True,blank=False)
        trademark=models.CharField("Marca", max_length=25,blank=False)
        model=models.CharField("Modelo", max_length=25,blank=False)
        category=models.ForeignKey(Categories,on_delete=models.CASCADE, blank=False, verbose_name="Categoría")
        owner=models.ForeignKey(Customer,on_delete=models.CASCADE,blank=False,verbose_name="Propietario")

        verbose_name = "Vechículo"
        verbose_name_plural = "Vechículos"
        ordering = ["license_plate"]
        
        def __str__(self):
            return f'{self.license_plate}'