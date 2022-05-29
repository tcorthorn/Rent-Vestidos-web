from dataclasses import fields
from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ('sku','cliente','fecha_reservada')
        widgets = {
            'sku':forms.TextInput(attrs={'class':'form-control','placeholder':'Sku del Vestido que reserva'}),
            'cliente':forms.TextInput(attrs={'class':'form-control','placeholder':'Cliente que reserva'}),
            'fecha_reservada':forms.DateInput(attrs={'class':'form-control','placeholder':'Fecha que reserva'}),



        }
