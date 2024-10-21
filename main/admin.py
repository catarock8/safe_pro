from django.contrib import admin
from .models import PlanCapacitacion, Empresa

# Register your models here.
@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email_contacto', 'rut_empresa', 'is_active', 'is_admin')
# Registrar el modelo PlanCapacitacion
@admin.register(PlanCapacitacion)
class PlanCapacitacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'expositor', 'empresa', 'descripcion')  # Campos mostrados en el admin
    search_fields = ('nombre', 'empresa__nombre')  # Habilita la búsqueda por nombre de capacitación o empresa