from django.db import models

class Voluntario(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Evento(models.Model):
    titulo = models.CharField(max_length=255)
    fecha = models.DateField()
    descripcion = models.TextField()
    voluntarios = models.ManyToManyField(Voluntario, blank=True)

    def __str__(self):
        return self.titulo
