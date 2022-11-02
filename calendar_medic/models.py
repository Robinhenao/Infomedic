from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=100, null=False, verbose_name='Nombre')
    apellido = models.CharField(max_length=100, null=False, verbose_name='Apellido')
    telefono = models.CharField(max_length=20, null=False, verbose_name='Telefono')
    edad = models.CharField(max_length=3, null=False, verbose_name='Edad')


class Paciente(Persona):
    genero = models.CharField(max_length=30, null=False, verbose_name='Genero')
    correo = models.CharField(max_length=100, null=False, verbose_name='Correo')
    direccion = models.CharField(max_length=100, null=False, verbose_name='Direccion')

    def __str__(self):
        return self.nombre

    class meta:
        db_table = "paciente"
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        ordering = ['id']


class Acompanante(Persona):
    parentesco = models.CharField(max_length=100, null=False, verbose_name='parentesco')

    def __str__(self):
        return self.nombre

    class meta:
        db_table = "acompanante"
        verbose_name = "Acompanante"
        verbose_name_plural = "Acompanantes"
        ordering = ['id']


class Cita(models.Model):
    fecha = models.DateField(verbose_name='Fecha definida')
    hora = models.TimeField(verbose_name='Fecha definida')
    lugar = models.CharField(max_length=100, null=False, verbose_name='Lugar')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    acompanante = models.ForeignKey(Acompanante, on_delete=models.CASCADE)
    costo = models.CharField(max_length=20, null=False, verbose_name='Costo')
    estado = models.CharField(max_length=40, null=False, verbose_name='Estado')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.lugar

    class meta:
        db_table = "cita"
        verbose_name = "Cita"
        verbose_name_plural = "Citas"
        ordering = ['id']
