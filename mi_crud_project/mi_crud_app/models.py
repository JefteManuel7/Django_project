from django.db import models

# Create your models here.
# mi_crud_app/models.py

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.nombre

