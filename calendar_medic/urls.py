from django.urls import path
from .views import *

urlpatterns = [
    path('agenda/', agenda, name='agenda'),
    path('agenda/make_paciente/', make_paciente, name="make_paciente"),
    path('agenda/make_acompanante/', make_acompanante, name="make_acompanante"),
    path('agenda/make_cita/', make_cita, name="make_cita"),
    path('agenda/delete/<int:project_id>', delete_cita, name="delete_cita"),
    path('agenda/update/<int:project_id>', update_cita, name="update_cita"),
]
