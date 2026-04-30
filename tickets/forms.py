from django import forms

from .models import Ticket

"""
Aquí se esta el cuestionario de se llena para crear la solicitud, el usuario solo escribe 
la solicitud y el sistema asigna automáticamente quién la creó y el estado inicial "Abierto".
Ya luego el administrador responde después desde Django Admin.
"""
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["titulo", "descripcion", "categoria"]
        labels = {
            "titulo": "Título",
            "descripcion": "Descripción",
            "categoria": "Categoría",
        }
        widgets = {
            "titulo": forms.TextInput(attrs={
                "placeholder": "Ingrese el título del ticket"
            }),
            "descripcion": forms.Textarea(attrs={
                "placeholder": "Describa la solicitud de soporte",
                "rows": 5
            }),
        }