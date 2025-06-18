from django.shortcuts import render, redirect
from .forms import SimuladorCreditoForm
from .models import SolicitudCredito
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required



def pagina_inicio(request):
    if request.method == "POST":
        form = SimuladorCreditoForm(request.POST)
        if form.is_valid():
            SolicitudCredito.objects.create(
                nombre_apellido=form.cleaned_data['nombre_apellido'],
                edad=form.cleaned_data['edad'],
                email=form.cleaned_data['email'],
                celular=form.cleaned_data['celular'],
                ingreso_mensual=form.cleaned_data['ingreso_mensual'],
                valor_propiedad=form.cleaned_data['valor_propiedad'],
                ahorros=form.cleaned_data['ahorros']
            )
            mensajeexito = "Solicitud enviada y almacenada correctamente"
        else:
            mensajeexito = "Hubo errores en el formulario"
    else:
        form = SimuladorCreditoForm()
        mensajeexito = None

    return render(request, 'mi_appss/index.html', {'form': form, 'mensajeexito': mensajeexito})

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'mi_appss/registro.html', {'form': form })

@login_required
def dashboard(request):
    return render(request,  'mi_appss/dashboard.html')

def nosotros(request):
    return render(request, 'mi_appss/nosotros.html')

def contacto(request):
    return render(request, 'mi_appss/contacto.html')