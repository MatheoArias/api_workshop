from django.db import models

class Employees_type(models.Model):
    jobs_names_cod=models.CharField("Código del puesto", max_length=50,unique=True,blank=False,null=False)
    jobs_names=models.CharField("Nombre del puesto", max_length=100,unique=True,blank=False,null=False)
    
    class Meta:
        verbose_name = "Puesto de trabajo"
        verbose_name_plural = "Puestos de trabajo"
        ordering = ["jobs_names_cod"]
    
    def __str__(self):
        
        return f'{self.jobs_names}'

class Employees(models.Model):
    
    names = models.CharField('Nombres y Apellidos', max_length=100,unique=False, null=False,blank=False)
    documents_type = models.CharField("Tipo de documento", max_length=50,unique=False, null=False,blank=False)
    documents_number=models.CharField("Número de documento", max_length=50,unique=True, null=False, blank=False)
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
