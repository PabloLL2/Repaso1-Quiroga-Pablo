from django.db import models

# Create your models here.

class Cerrajero(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    desempleado = models.BooleanField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Futbolista(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    club_futbol = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.club_futbol}'


class Actor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    pelicula = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.pelicula}'