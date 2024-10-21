from django.urls import path
from . import views

urlpatterns = [
    #urls para cliente
    path('', views.home_cliente, name='home_cliente'),
    path('capacitaciones/cliente/', views.capacitaciones_cliente, name='capacitaciones_cliente'),
    path('mis_evaluaciones/cliente/', views.mis_evaluaciones_cliente, name='mis_evaluaciones_cliente'),
    path('visitas_medicas/cliente/', views.visitas_medicas_cliente, name='visitas_medicas_cliente'),
    #urls para ingeniero
    path('home/ingeniero/', views.home_ingeniero, name='home_ingeniero'),
    path('capacitaciones/ingeniero/', views.capacitaciones_ingeniero, name='capacitaciones_ingeniero'),
    path('evaluaciones/ingeniero/', views.evaluaciones_ingeniero, name='evaluaciones_ingeniero'),
    path('visitas_medicas/ingeniero/', views.visitas_medicas_ingeniero, name='visitas_medicas_ingeniero'),
    #urls para supervisor
    path('home/supervisor/', views.home_supervisor, name='home_supervisor'),
    path('capacitaciones/supervisor/', views.capacitaciones_supervisor, name='capacitaciones_supervisor'),
    path('evaluaciones/supervisor/', views.evaluaciones_supervisor, name='evaluaciones_supervisor'),
    path('visitas_medicas/supervisor/', views.visitas_medicas_supervisor, name='visitas_medicas_supervisor'),
    #urls para tecnico
    path('home/tecnico/', views.home_tecnico, name='home_tecnico'),
    path('capacitaciones/tecnico/', views.capacitaciones_tecnico, name='capacitaciones_tecnico'),
    path('evaluaciones/tecnico/', views.evaluaciones_tecnico, name='evaluaciones_tecnico'),
    path('visitas_medicas/tecnico/', views.visitas_medicas_tecnico, name='visitas_medicas_tecnico'),
    #urls para usuarios
    path('login/usuarios/', views.login, name='login'),
    path('register/usuarios/', views.register, name='register'),

    
]