from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_cliente, name='home_cliente' ),
    #urls para cliente
    path('cliente/home/', views.home_cliente, name='home_cliente'),
    path('cliente/capacitaciones/', views.capacitaciones_cliente, name='capacitaciones_cliente'),
    path('cliente/mis_evaluaciones/', views.mis_evaluaciones_cliente, name='mis_evaluaciones_cliente'),
    path('cliente/visitas_medicas/', views.visitas_medicas_cliente, name='visitas_medicas_cliente'),
    #urls para ingeniero
    path('ingeniero/home/', views.home_ingeniero, name='home_ingeniero'),
    path('ingeniero/capacitaciones/', views.capacitaciones_ingeniero, name='capacitaciones_ingeniero'),
    path('ingeniero/evaluaciones/', views.evaluaciones_ingeniero, name='evaluaciones_ingeniero'),
    path('ingeniero/visitas_medicas/', views.visitas_medicas_ingeniero, name='visitas_medicas_ingeniero'),
    #urls para supervisor
    path('supervisor/home/', views.home_supervisor, name='home_supervisor'),
    path('supervisor/capacitaciones/', views.capacitaciones_supervisor, name='capacitaciones_supervisor'),
    path('supervisor/evaluaciones/', views.evaluaciones_supervisor, name='evaluaciones_supervisor'),
    path('supervisor/visitas_medicas/', views.visitas_medicas_supervisor, name='visitas_medicas_supervisor'),
    path('supervisor/capacitaciones/agregar/', views.agregar_plan_supervisor, name='agregar_plan_supervisor'),
    path('supervisor/capacitaciones/asistencia/<int:plan_id>/', views.ver_asistencia_supervisor, name='ver_asistencia_supervisor'),
    path('supervisor/capacitaciones/asistencia/<int:plan_id>/agregar/', views.agregar_asistencia_supervisor, name='agregar_asistencia_supervisor'),
    #urls para tecnico
    path('tecnico/home/', views.home_tecnico, name='home_tecnico'),
    path('tecnico/capacitaciones/', views.capacitaciones_tecnico, name='capacitaciones_tecnico'),
    path('tecnico/evaluaciones/', views.evaluaciones_tecnico, name='evaluaciones_tecnico'),
    path('tecnico/visitas_medicas/', views.visitas_medicas_tecnico, name='visitas_medicas_tecnico'),
    #urls para usuarios
    path('usuarios/login/', views.login_view, name='login'),
    path('usuarios/register/', views.register, name='register'),

    
]