from django.forms import ModelForm
from .models import Reserva
import datetime
from django.core.exceptions import ValidationError

class ReservaModelForm(ModelForm):
    class Meta:
        model = Reserva
        fields = ('sku','cliente','fecha_reservada')
        
    def clean_fecha_reservada(self):
       data = self.cleaned_data['fecha_reservada']

       #Check date is not in past.
       if data < datetime.date.today():
           raise ValidationError(('Invalid date - renewal in past'))

       #Check date is in range librarian allowed to change (+4 weeks)
       if data > datetime.date.today() + datetime.timedelta(weeks=4):
           raise ValidationError(('Invalid date - renewal more than 4 weeks ahead'))

       # Remember to always return the cleaned data.
       return data

    