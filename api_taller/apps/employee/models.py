from django.db import models
from apps.customer.models import DocumentType

"""
Example:
    "id": 2,
    "jobs_names_cod": "TC-002",
    "jobs_names": "Vendedor
"""
class Employees_type(models.Model):
    jobs_names_cod=models.CharField("Código del puesto", max_length=50,unique=True,blank=False,null=False)
    jobs_names=models.CharField("Nombre del puesto", max_length=100,unique=True,blank=False,null=False)
    
    class Meta:
        verbose_name = "Puesto de trabajo"
        verbose_name_plural = "Puestos de trabajo"
        ordering = ["jobs_names_cod"]
    
    def __str__(self):
        
        return f'{self.jobs_names_cod} - {self.jobs_names}'
    
"""
Example:
    "id": 1,
    "employees_type_id": {
        "id": 1,
        "jobs_names_cod": "TC-001",
        "jobs_names": "Técnico"
    },
    "documents_type": {
        "id": 1,
        "types": "C.C.",
        "name": "Cédula de ciudania"
    },
    "names": "Mateo Arias Correa",
    "document_number": "1025871059",
    "telephone_number": 3128965989,
    "address_residence": "CARREA 95B #52 B-45",
    "email_address": "teoarco@gmail.com",
    "salarys_value": "1200000.00
""" 

class Employees(models.Model):
    
    names = models.CharField('Nombres y Apellidos', max_length=100,unique=False, null=False,blank=False)
    documents_type = models.ForeignKey(DocumentType, verbose_name="Tipo de documento", on_delete=models.CASCADE)
    document_number=models.CharField("Número de documento", max_length=50,unique=True, null=False, blank=False)
    telephone_number=models.IntegerField("Número de telephone",unique=False, null=False, blank=False)
    address_residence=models.CharField("Direccion", max_length=200, unique=False, null=False, blank=False)
    email_address=models.EmailField('Correo Electrónico',unique=False, null=False, blank=False)
    employees_type_id=models.ForeignKey(Employees_type, verbose_name="Puesto de trabajo", on_delete=models.CASCADE)
    salarys_value=models.DecimalField("Salario Mensual", max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ["names"]
    
    def __str__(self):
        
        return f'{self.names}'
