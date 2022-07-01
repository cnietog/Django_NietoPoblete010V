from django.urls import path 
from .views import inicio, somos, contacto, utilidades, catalogo, galeria_cliente, registro, enviado, inventario, inventario_crear, inventario_modificar, inventario_eliminar, peticiones_contacto, contacto_eliminar, cliente, cliente_crear, cliente_modificar, cliente_eliminar, catalogo_semilla, catalogo_arboles, catalogo_arbusto, catalogo_flores, catalogo_macetero, catalogo_herramientas
urlpatterns=[ 
    path ('', inicio, name="inicio"),
    path ('somos/', somos, name="somos"),
    path ('contacto/', contacto, name="contacto"),
    path ('utilidades/', utilidades, name="utilidades"),
    path ('catalogo/', catalogo, name="catalogo"),
    path ('galeria_cliente/', galeria_cliente, name="galeria_cliente"),
    path ('registro/', registro, name="registro"),
    path ('enviado/', enviado, name="enviado"),
    path ('inventario/', inventario, name="inventario"),
    path ('inventario_crear/', inventario_crear, name="inventario_crear"),
    path ('inventario_modificar/<id>', inventario_modificar, name="inventario_modificar"),
    path ('inventario_eliminar/<id>', inventario_eliminar, name="inventario_eliminar"),
    path ('peticiones_contacto/', peticiones_contacto, name="peticiones_contacto"),
    path ('contacto_eliminar/<id>', contacto_eliminar, name="contacto_eliminar"),
    path ('cliente/', cliente, name="cliente"),
    path ('cliente_crear/', cliente_crear, name="cliente_crear"),
    path ('cliente_modificar/<id>', cliente_modificar, name="cliente_modificar"),
    path ('cliente_eliminar/<id>', cliente_eliminar, name="cliente_eliminar"),
    path ('catalogo_semilla/', catalogo_semilla, name="catalogo_semilla"),
    path ('catalogo_arboles/', catalogo_arboles, name="catalogo_arboles"),
    path ('catalogo_arbusto/', catalogo_arbusto, name="catalogo_arbusto"),
    path ('catalogo_flores/', catalogo_flores, name="catalogo_flores"),
    path ('catalogo_macetero/', catalogo_macetero, name="catalogo_macetero"),
    path ('catalogo_herramientas/', catalogo_herramientas, name="catalogo_herramientas"),
    
    ]