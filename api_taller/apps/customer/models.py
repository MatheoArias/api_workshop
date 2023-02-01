from django.db import models

class Customer(models.Model):
         
    names = models.CharField('Nombres y Apellidos', max_length=100,unique=False, null=False,blank=False)
    documents_type = models.CharField("Tipo de documento", max_length=50, unique=False, null=False,blank=False)
    documents_number=models.CharField("Número de documento", max_length=50,unique=True, null=False, blank=False)
    telephone_number=models.IntegerField("Número de telephone",unique=False, null=False, blank=False)
    address_residence=models.CharField("Direccion", max_length=200, unique=False, null=False, blank=False)
    email_address=models.EmailField('Correo Electrónico',unique=False, null=False, blank=False)

    verbose_name = "Cliente"
    verbose_name_plural = "Clientes"
    ordering = ["documents_number"]
    
    def __str__(self):
            return f'{self.names}'