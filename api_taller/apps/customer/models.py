from django.db import models

"""Example DocumentType:
document_Type = C.C.
IMPORTANT:this model is based in colombian political"""

class DocumentType(models.Model):
    types = models.CharField("Abreviatura", max_length=50, unique=True, null=False, blank=False)
    name=models.CharField("Nombre", max_length=100 , unique=True, null=True, blank=False)
    "Change null=false"
    
    verbose_name = "Tipo de documento"
    verbose_name_plural = "Tipos de documentos"
    ordering = ["type"]
    
    def __str__(self):
            return f'{self.types} - {self.name}'

""" Example Customer:
    names:Mateo Arias Correa
    document_type:C.C
    telephone_number:3128794587
    residence_address:carrera 28 # 68-45
    email_address:teoarco@gmail.com
"""

class Customer(models.Model):
         
    names = models.CharField('Nombres y Apellidos', max_length=100,unique=False, null=False,blank=False)
    document_type = models.ForeignKey(DocumentType, verbose_name="Tipo de documento", on_delete=models.CASCADE)
    document_number=models.CharField("Número de documento", max_length=50,unique=True, null=False, blank=False)
    telephone_number=models.IntegerField("Número de telephone",unique=False, null=False, blank=False)
    telephone_cel=models.IntegerField("Número de celular",unique=False, null=True, blank=False)
    residence_address=models.CharField("Direccion", max_length=200, unique=False, null=False, blank=False)
    email_address=models.EmailField('Correo Electrónico',unique=False, null=False, blank=False)
    "Change null=false"
    
    verbose_name = "Cliente"
    verbose_name_plural = "Clientes"
    ordering = ["documents_number"]
    
    def __str__(self):
            return f'{self.names}'