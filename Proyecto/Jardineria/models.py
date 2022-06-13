from django.db import models

# Create your models here.

class Contacto (models.Model):
    nombre = models.CharField(max_length=40 ,primary_key=True, verbose_name='Nombre')
    email = models.CharField(max_length=40 ,verbose_name='Correo')
    telefono = models.IntegerField(verbose_name='Telefono')
    comentario = models.CharField(max_length=140 ,verbose_name='Comentario')
    def __str__(self):
        return self.nombre


class Categoria (models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='ID de Categoría')
    nombreCategoria = models.CharField(max_length=40, verbose_name='Nombre de Categoría')

    def __str__(self):
        return self.nombreCategoria

class Producto (models.Model):
    foto = models.ImageField(upload_to="Producto", null=True, blank=True)
    nombre = models.CharField(max_length=40 ,primary_key=True, verbose_name='Nombre')
    cantidad = models.IntegerField(verbose_name='Cantidad Disponible')
    precio = models.IntegerField(verbose_name='Precio')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre


class Cliente (models.Model):
    nombre = models.CharField(max_length=40 ,primary_key=True, verbose_name='Nombre')
    perfil = models.ImageField(upload_to="Cliente", null=True , blank=True)
    rut = models.CharField(max_length=40 ,verbose_name='Rut')
    email = models.CharField(max_length=40 ,verbose_name='Correo')
    direccion = models.CharField(max_length=40 ,verbose_name='Direccion')
    comuna = models.CharField(max_length=40 ,verbose_name='Comuna')
    region = models.CharField(max_length=40 ,verbose_name='Region')
    telefono = models.IntegerField(verbose_name='Telefono')
    def __str__(self):
        return self.nombre

