from django import forms

class SimuladorCreditoForm(forms.Form):
    nombre_apellido = forms.CharField(label='Nombre y Apellido',max_length=255,error_messages={'required': 'Este campo es obligatorio','max_length': 'Maximo 255 caracteres permitidos'})
    edad = forms.IntegerField(label='Edad',min_value=18,error_messages={'required': 'Este campo es obligatorio','min_value': 'Debes tener al menos 18 años'})
    email = forms.EmailField(label='Correo electronico',error_messages={'required': 'Este campo es obligatorio','invalid': 'Ingresa un correo electronico valido'})
    celular = forms.CharField(label='Celular',max_length=20,error_messages={'required': 'Este campo es obligatorio','max_length': 'El numero no puede tener mas de 20 caracteres'})
    ingreso_mensual = forms.DecimalField(label='Ingreso bruto mensual (en pesos)',max_digits=12,decimal_places=2,error_messages={'required': 'Este campo es obligatorio','invalid': 'Debe ser un numero valido'})
    valor_propiedad = forms.DecimalField(label='Valor de la propiedad (en pesos)',max_digits=12,decimal_places=2,error_messages={'required': 'Este campo es obligatorio','invalid': 'Debe ser un numero valido'})
    ahorros = forms.DecimalField(label='Ahorros disponibles (en pesos)',max_digits=12,decimal_places=2,error_messages={'required': 'Este campo es obligatorio','invalid': 'Debe ser un numero valido'})
