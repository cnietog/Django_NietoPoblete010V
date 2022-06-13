from django.contrib import admin
from .models import Contacto, Categoria, Producto, Cliente
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Contacto)
admin.site.register(Producto)
admin.site.register(Cliente)