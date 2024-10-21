from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class EmpresaManager(BaseUserManager):
    def create_user(self, email_contacto, nombre, rut_empresa, password=None):
        if not email_contacto:
            raise ValueError('La empresa debe tener un email de contacto')
        if not rut_empresa:
            raise ValueError('La empresa debe tener un RUT válido')
        
        empresa = self.model(
            email_contacto=self.normalize_email(email_contacto),
            nombre=nombre,
            rut_empresa=rut_empresa
        )
        empresa.set_password(password)  # Almacena la contraseña encriptada
        empresa.save(using=self._db)
        return empresa

    def create_superuser(self, email_contacto, nombre, rut_empresa, password=None):
        empresa = self.create_user(
            email_contacto=email_contacto,
            nombre=nombre,
            rut_empresa=rut_empresa,
            password=password,
        )
        empresa.is_admin = True
        empresa.save(using=self._db)
        return empresa

class Empresa(AbstractBaseUser):
    nombre = models.CharField(max_length=255, unique=True)
    email_contacto = models.EmailField()
    direccion = models.CharField(max_length=255)
    rut_empresa = models.CharField(max_length=12, unique=True)
    is_active = models.BooleanField(default=True)  # Indica si la empresa está activa
    is_admin = models.BooleanField(default=False)  # Indica si es un superusuario (admin)

    objects = EmpresaManager()

    USERNAME_FIELD = 'email_contacto'
    REQUIRED_FIELDS = ['nombre', 'rut_empresa']

    def __str__(self):
        return self.nombre
    
    @property
    def is_staff(self):
        return self.is_admin



#modelos para supervisor
class PlanCapacitacion(models.Model):
    nombre = models.CharField(max_length=255)
    fecha = models.DateField()
    expositor = models.CharField(max_length=255)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)  # Relación con Empresa
    descripcion = models.TextField()  # Nueva descripción del plan de capacitación

    def __str__(self):
        return f"{self.nombre} - {self.empresa.nombre}"

class Asistencia(models.Model):
    plan = models.ForeignKey(PlanCapacitacion, on_delete=models.CASCADE, related_name='asistencias')
    nombre_participante = models.CharField(max_length=255)
    empresa_participante = models.CharField(max_length=255)
    fecha_asistencia = models.DateField()

    def __str__(self):
        return f"{self.nombre_participante} - {self.plan.nombre}"



