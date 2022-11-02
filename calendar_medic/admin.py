from django.contrib import admin
from calendar_medic.models import Paciente, Acompanante, Cita

# Register your models here.
admin.site.register([Paciente, Acompanante, Cita])
