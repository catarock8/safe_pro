from django.shortcuts import render


# Create your views here.

#views para cliente
def home_cliente(request):
    return render(request, 'cliente/home.html')

def capacitaciones_cliente(request):
    return render(request, 'cliente/capacitaciones.html')

def mis_evaluaciones_cliente(request):
    return render(request, 'cliente/mis_evaluaciones.html')

def visitas_medicas_cliente(request):
    return render(request, 'cliente/visitas_medicas.html')

#views para ingeniero
def home_ingeniero(request):
    return render(request, 'ingeniero/home.html')

def capacitaciones_ingeniero(request):
    return render(request, 'ingeniero/capacitaciones.html')

def evaluaciones_ingeniero(request):
    return render(request, 'ingeniero/evaluaciones.html')

def visitas_medicas_ingeniero(request):
    return render(request, 'ingeniero/visitas_medicas.html')

#views para supervisor
def home_supervisor(request):
    return render(request, 'supervisor/home.html')

def capacitaciones_supervisor(request):
    return render(request, 'supervisor/capacitaciones.html')

def evaluaciones_supervisor(request):
    return render(request, 'supervisor/evaluaciones.html')

def visitas_medicas_supervisor(request):
    return render(request, 'supervisor/visitas_medicas.html')

#views para tecnico
def home_tecnico(request):
    return render(request, 'tecnico/home.html')

def capacitaciones_tecnico(request):
    return render(request, 'tecnico/capacitaciones.html')

def evaluaciones_tecnico(request):
    return render(request, 'tecnico/evaluaciones.html')

def visitas_medicas_tecnico(request):
    return render(request, 'tecnico/visitas_medicas.html')

#views para usuarios
def login(request):
    return render(request, 'usuarios/login.html')

def register(request):
    return render(request, 'usuarios/register.html')