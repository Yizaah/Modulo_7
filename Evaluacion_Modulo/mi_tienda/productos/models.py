from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class DetalleProducto(models.Model):
    producto = models.OneToOneField("Producto", on_delete=models.CASCADE, null=True, blank=True)
    dimensiones = models.CharField(max_length=100, blank=True, null=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Detalles de {self.producto.nombre if self.producto else 'Producto sin asignar'}"



class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    # Relación MUCHOS A UNO: muchos productos  una categoría
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='productos'   # permite categoria.productos.all()
    )

    # Relación MUCHOS A MUCHOS: producto etiquetas
    etiquetas = models.ManyToManyField(
        Etiqueta,
        blank=True,
        related_name='productos'
    )

    def __str__(self):
        return self.nombre
