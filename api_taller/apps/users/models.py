from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    def _create_user(self, email, name,last_name, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            email = email,
            name = name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, name,last_name, password=None, **extra_fields):
        return self._create_user( email, name,last_name, password, False, False, **extra_fields)

    def create_superuser(self, email, name,last_name, password=None, **extra_fields):
        return self._create_user(email, name,last_name, password, True, True, **extra_fields)
    

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField('Correo Electrónico',max_length = 255, unique = True)
    name = models.CharField('Nombres', max_length = 255, blank = True, null = True)
    last_name = models.CharField('Apellidos', max_length = 255, blank = True, null = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    objects = UserManager()
    
    verbose_name = "Usuario"
    verbose_name_plural = "Usuarios"
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','last_name']
    

    def __str__(self):
        return f'{self.name} - {self.last_name}'
    
