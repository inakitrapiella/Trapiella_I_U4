from django.shortcuts import render, redirect
from .forms import SimuladorCreditoForm
from .models import SolicitudCredito
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def pagina_inicio(request):
    mensajeexito = None
    nombre = None
    total_pagar = None
    cuotas = None
    cuota_mensual = None

    if request.method == "POST":
        form = SimuladorCreditoForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre_apellido']
            edad = form.cleaned_data['edad']
            email = form.cleaned_data['email']
            celular = form.cleaned_data['celular']
            ingreso_bruto = float(form.cleaned_data['ingreso_mensual'])
            valor_propiedad = float(form.cleaned_data['valor_propiedad'])
            ahorros = float(form.cleaned_data['ahorros'])


            interes = 0.065
            plazo_anios = 20
            cuotas = plazo_anios * 12
            monto_solicitado = valor_propiedad - ahorros

            interes_total = monto_solicitado * interes
            total_pagar = monto_solicitado + interes_total
            cuota_mensual = total_pagar / cuotas


            SolicitudCredito.objects.create(
                nombre_apellido=nombre,
                edad=edad,
                email=email,
                celular=celular,
                ingreso_mensual=ingreso_bruto,
                valor_propiedad=valor_propiedad,
                ahorros=ahorros
            )

            mensajeexito = "Solicitud enviada y almacenada correctamente"
        else:
            mensajeexito = "Hubo errores en el formulario"
    else:
        form = SimuladorCreditoForm()

    return render(request, 'mi_appss/index.html', {
        'form': form,
        'mensajeexito': mensajeexito,
        'nombre': nombre,
        'total_pagar': total_pagar,
        'plazo': cuotas,
        'cuota': cuota_mensual
    })

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