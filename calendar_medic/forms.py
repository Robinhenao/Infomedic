from django import forms
from django.forms import Form,ModelForm
from calendar_medic.models import Paciente, Acompanante, Cita


class date_picker_input(forms.DateInput):
    input_type = 'date'


class time_picker(forms.DateTimeInput):
    input_type = 'time'


class form_paciente(ModelForm):
    class Meta:
        model = Paciente
        fields = ('nombre', 'apellido', 'telefono', 'edad', 'genero','correo','direccion')


class form_acompanante(ModelForm):
    class Meta:
        model = Acompanante
        fields = ('nombre', 'apellido', 'telefono', 'edad', 'parentesco')


class form_cita(ModelForm):
    class Meta:
        model = Cita
        fields = ('fecha','hora', 'lugar', 'paciente', 'acompanante', 'costo', 'estado')
        widgets = {'fecha': date_picker_input(),'hora':time_picker(), }