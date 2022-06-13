from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Categoria, Producto, Contacto, Cliente
from django.conf import settings
from django.core.files.storage import FileSystemStorage


class ProductoForm(forms.ModelForm):

    class Meta:  
        model= Producto
        fields = ['foto', 'nombre', 'cantidad', 'precio', 'categoria']
        labels ={
            'foto': 'Foto',
            'nombre': 'Nombre', 
            'cantidad': 'Cantidad', 
            'precio': 'Precio', 
            'categoria': 'Categoría',
        }
        widgets={
            'foto': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'foto'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el Nombre del Producto', 
                    'id': 'nombre'
                }
            ), 
            'cantidad': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese la cantidad', 
                    'id': 'cantidad'
                }
            ), 
            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el precio', 
                    'id': 'precio'
                }
            ), 
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria',
                }
            )

        }







class ContactoForm(forms.ModelForm):

    class Meta: 
        model= Contacto
        fields = ['nombre', 'email', 'telefono', 'comentario']
        labels ={
            'nombre': 'Nombre', 
            'email': 'Correo Electronico', 
            'telefono': 'Telefono', 
            'comentario': 'Comentario',
        }
        widgets={
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su Nombre', 
                    'id': 'nombre'
                }
            ), 
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'MiCorreo@Dominio.cl', 
                    'id': 'cantidad'
                }
            ), 
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': '+56 9 XXXXXXXX', 
                    'id': 'precio'
                }
            ), 
            'comentario': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Max 100 Carácteres',
                    'id': 'comentario'
                }
            )

        }

 

class ClienteForm(forms.ModelForm):

    class Meta:  
        model= Cliente
        fields = ['nombre', 'perfil', 'rut', 'email', 'direccion','comuna', 'region', 'telefono']
        labels ={
            'nombre': 'Nombre', 
            'perfil': 'Perfil', 
            'rut': 'Rut', 
            'email': 'Email', 
            'direccion': 'Direccion',
            'comuna': 'Comuna',
            'region': 'Region',
            'telefono': 'Telefono',
        }
        widgets={
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el Nombre y Apellido', 
                    'id': 'nombre'
                }
            ),
            'perfil': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'perfil'
                }
            ),  
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el Rut del Cliente', 
                    'id': 'rut'
                }
            ), 
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'MiCorreo@Dominio.cl', 
                    'id': 'email'
                }
            ), 
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'direccion',
                    'placeholder': 'Ingrese su direccion', 
                }
            ),
            'comuna': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'comuna',
                    'placeholder': 'Ingrese su Comuna', 
                }
            ),
            'region': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'region',
                    'placeholder': 'Ingrese su Region', 
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'telefono',
                    'placeholder': '+56 9 XXXXXXXX', 
                }
            )


        }     

class CategoriaForm(forms.ModelForm):

    class Meta: 
        model= Categoria
        fields = ['idCategoria', 'nombreCategoria']
        labels ={
            'idCategoria': 'ID Categoria', 
            'nombreCategoria': 'Nombre Categoria', 

        }
        widgets={
            'idCategoria': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el ID', 
                    'id': 'idCategoria'
                }
            ), 
            'nombreCategoria': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el Nombre', 
                    'id': 'nombreCategoria'
                }
            )

        }