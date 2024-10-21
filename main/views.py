from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import PlanCapacitacion, Asistencia, Empresa
from .forms import RegistroEmpresaForm


# Create your views here.

#### views para cliente
def home_cliente(request):
    return render(request, 'cliente/home.html')

def capacitaciones_cliente(request):
    return render(request, 'cliente/capacitaciones.html')

def mis_evaluaciones_cliente(request):
    return render(request, 'cliente/mis_evaluaciones.html')

def visitas_medicas_cliente(request):
    return render(request, 'cliente/visitas_medicas.html')
####


#### views para ingeniero
def home_ingeniero(request):
    return render(request, 'ingeniero/home.html')

def capacitaciones_ingeniero(request):
    return render(request, 'ingeniero/capacitaciones.html')

def evaluaciones_ingeniero(request):
    return render(request, 'ingeniero/evaluaciones.html')

def visitas_medicas_ingeniero(request):
    return render(request, 'ingeniero/visitas_medicas.html')
####


#### views para supervisor
def home_supervisor(request):
    return render(request, 'supervisor/home.html')

def capacitaciones_supervisor(request):
    planes = PlanCapacitacion.objects.all()
    empresas = Empresa.objects.all()  # Obtener todas las empresas
    return render(request, 'supervisor/capacitaciones.html', {'planes': planes})

def agregar_plan_supervisor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        fecha = request.POST.get('fecha')
        expositor = request.POST.get('expositor')
        descripcion = request.POST.get('descripcion')  # Descripción del plan
        empresa_id = request.POST.get('empresa')  # Obtenemos la empresa seleccionada por su ID

        empresa = Empresa.objects.get(id=empresa_id)  # Buscamos la empresa en la base de datos
        PlanCapacitacion.objects.create(
            nombre=nombre, 
            fecha=fecha, 
            expositor=expositor, 
            descripcion=descripcion,  # Guardamos la descripción del plan
            empresa=empresa
        )
        return redirect('capacitaciones_supervisor')

    # Obtenemos todas las empresas registradas
    empresas = Empresa.objects.all()  
    return render(request, 'supervisor/agregar_plan.html', {'empresas': empresas})




def ver_asistencia_supervisor(request, plan_id):
    plan = PlanCapacitacion.objects.get(id=plan_id)
    asistencias = plan.asistencias.all()
    return render(request, 'supervisor/ver_asistencia.html', {'plan': plan, 'asistencias': asistencias})

def agregar_asistencia_supervisor(request, plan_id):
    if request.method == 'POST':
        archivo_asistencia = request.FILES['archivo_asistencia']
        # Aquí podrías procesar el archivo de asistencia, por ahora agregamos un ejemplo simple.
        nombre_participante = "Participante Ejemplo"
        empresa_participante = "Empresa Ejemplo"
        Asistencia.objects.create(plan_id=plan_id, nombre_participante=nombre_participante, empresa_participante=empresa_participante, fecha_asistencia=PlanCapacitacion.objects.get(id=plan_id).fecha)
        return redirect('ver_asistencia_supervisor', plan_id=plan_id)

    return render(request, 'supervisor/agregar_asistencia.html', {'plan_id': plan_id})


def evaluaciones_supervisor(request):
    return render(request, 'supervisor/evaluaciones.html')

def visitas_medicas_supervisor(request):
    return render(request, 'supervisor/visitas_medicas.html')
####


#### views para tecnico
def home_tecnico(request):
    return render(request, 'tecnico/home.html')

def capacitaciones_tecnico(request):
    return render(request, 'tecnico/capacitaciones.html')

def evaluaciones_tecnico(request):
    return render(request, 'tecnico/evaluaciones.html')

def visitas_medicas_tecnico(request):
    return render(request, 'tecnico/visitas_medicas.html')
####


#### views para usuarios que se registran (empresas)

def login_view(request):
    if request.method == 'POST':
        email_contacto = request.POST['username']  # Aquí obtienes el email del formulario
        password = request.POST['password']  # Y aquí la contraseña del formulario
        user = authenticate(request, username=email_contacto, password=password)  # Autenticas al usuario

        if user is not None:
            login(request, user)  # Aquí es donde pasas el 'user' autenticado a la función 'login'
            return redirect('home_empresa')  # Redirige al home de la empresa u otra vista
        else:
            return render(request, 'usuarios/login.html', {'error': 'Credenciales incorrectas'})
    
    return render(request, 'usuarios/login.html')

def register(request):
    if request.method == 'POST':
        form = RegistroEmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroEmpresaForm()
    return render(request, 'usuarios/register.html', {'form': form})



