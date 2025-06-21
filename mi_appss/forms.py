from django import forms

class SimuladorCreditoForm(forms.Form):
    nombre_apellido = forms.CharField(
        label='Nombre y Apellido',
        max_length=255,
        widget=forms.TextInput(attrs={
            'placeholder': 'Nombre y Apellido',
            'name': 'nombre_apellido'
        }),
        error_messages={
            'required': 'Este campo es obligatorio',
            'max_length': 'Máximo 255 caracteres permitidos'
        }
    )

    edad = forms.IntegerField(
        label='Edad',
        min_value=18,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Edad',
            'name': 'edad'
        }),
        error_messages={
            'required': 'Este campo es obligatorio',
            'min_value': 'Debes tener al menos 18 años'
        }
    )

    email = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={
            'placeholder': 'Correo electrónico',
            'name': 'email'
        }),
        error_messages={
            'required': 'Este campo es obligatorio',
            'invalid': 'Ingresa un correo electrónico válido'
        }
    )

    celular = forms.CharField(
        label='Celular',
        max_length=20,
        widget=forms.TextInput(attrs={
            'placeholder': 'Celular',
            'name': 'celular'
        }),
        error_messages={
            'required': 'Este campo es obligatorio',
            'max_length': 'El número no puede tener más de 20 caracteres'
        }
    )

    ingreso_mensual = forms.DecimalField(
        label='Ingreso bruto mensual (en pesos)',
        max_digits=12,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Ingreso bruto mensual (en pesos)',
            'name': 'ingreso_mensual'
        }),
        error_messages={
            'required': 'Este campo es obligatorio',
            'invalid': 'Debe ser un número válido'
        }
    )

    valor_propiedad = forms.DecimalField(
        label='Valor de la propiedad (en pesos)',
        max_digits=12,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Valor de la propiedad (en pesos)',
            'name': 'valor_propiedad'
        }),
        error_messages={
            'required': 'Este campo es obligatorio',
            'invalid': 'Debe ser un número válido'
        }
    )

    ahorros = forms.DecimalField(
        label='Ahorros disponibles (en pesos)',
        max_digits=12,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Ahorros disponibles (en pesos)',
            'name': 'ahorros'
        }),
        error_messages={
            'required': 'Este campo es obligatorio',
            'invalid': 'Debe ser un número válido'
        }
    )