from django.db import models
from django.contrib.auth.models import User  # Opcional si quieres vincular Estudiante con un usuario

# Profesor
class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    departamento = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Curso
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='cursos',null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"

# Estudiante
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()
    # opcional: vincular con usuario de Django
    # usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre

# Perfil del estudiante
class Perfil(models.Model):
    estudiante = models.OneToOneField(Estudiante, on_delete=models.CASCADE, related_name='perfil')
    biografia = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='perfiles/', blank=True, null=True)
    redes_sociales = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.estudiante.nombre}"

# Entidad intermedia para Inscripción
class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=50, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo')
    nota_final = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        unique_together = ('estudiante', 'curso')  # evita duplicar inscripción

    def __str__(self):
        return f"{self.estudiante.nombre} en {self.curso.nombre}"
