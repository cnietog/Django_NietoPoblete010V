from django.shortcuts import render, redirect
from django.views.decorators import csrf
from .models import Producto, Contacto, Cliente
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import ProductoForm, ContactoForm, ClienteForm


#Pagina de Inicio
def inicio (request):
    return render(request, 'inicio.html')

def somos (request):
    return render(request, 'Somos.html')

#def contacto (request):
#    return render(request, 'Contacto.html')

def utilidades (request):
    return render(request, 'Utilidades.html')

def catalogo (request):
    return render(request, 'Catalogo.html')

def galeria_cliente (request):
    return render(request, 'Galeria_cliente.html')

def registro (request):
    return render(request, 'Registro.html')

def enviado (request):
    return render(request, 'Enviado.html')

def inventario (request):
    producto = Producto.objects.all()

    datos = {
        'producto' : producto
        }
    return render(request, 'Inventario.html',datos)

def inventario_crear (request):

    if request.method=='POST':
        producto_form = ProductoForm(request.POST, files=request.FILES)
        if producto_form.is_valid():
            producto_form.save()
            return redirect ('inventario')
    else:
        producto_form = ProductoForm()
    return render(request, 'Inventario_crear.html', {'producto_form': producto_form})


def inventario_modificar(request, id):
    producto = Producto.objects.get(nombre=id)
    datos = {
        'form': ProductoForm(instance = producto)
    }
    if request.method=='POST':
        formulario = ProductoForm(data=request.POST, instance = producto , files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('inventario')
    return render(request, 'inventario_modificar.html', datos)

def contacto (request):

    if request.method=='POST':
        contacto_form = ContactoForm(request.POST)
        if contacto_form.is_valid():
            contacto_form.save()
            return redirect ('enviado')
    else:
        contacto_form = ContactoForm()
    return render(request, 'Contacto.html', {'contacto_form': contacto_form})

def peticiones_contacto (request):
    contacto = Contacto.objects.all()

    datos = {
        'contacto' : contacto
        }
    return render(request, 'peticiones_contacto.html',datos)

def inventario_eliminar(request, id):
    producto = Producto.objects.get(nombre=id)
    producto.delete()
    return redirect('inventario')

def contacto_eliminar(request, id):
    contacto = Contacto.objects.get(nombre=id)
    contacto.delete()
    return redirect('peticiones_contacto')



def cliente (request):
    cliente = Cliente.objects.all()

    datos = {
        'cliente' : cliente
        }
        
    return render(request, 'Cliente.html',datos)

def cliente_crear (request):

    if request.method=='POST':
        cliente_form = ClienteForm(request.POST, files=request.FILES)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect ('cliente')
    else:
        cliente_form = ClienteForm()
    return render(request, 'Cliente_crear.html', {'cliente_form': cliente_form})


def cliente_modificar(request, id):
    cliente = Cliente.objects.get(nombre=id)
    datos = {
        'form': ClienteForm(instance = cliente)
    }
    if request.method=='POST':
        formulario = ClienteForm(data=request.POST, instance = cliente , files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('cliente')
    return render(request, 'Cliente_modificar.html', datos)


def cliente_eliminar(request, id):
    cliente = Cliente.objects.get(nombre=id)
    cliente.delete()
    return redirect('cliente')



def catalogo_semilla (request):
    producto = Producto.objects.filter(categoria = 1)

    datos = {
        'producto' : producto
        }
    return render(request, 'Catalogo_semilla.html',datos)

def catalogo_arboles (request):
    producto = Producto.objects.filter(categoria = 4)

    datos = {
        'producto' : producto
        }
    return render(request, 'Catalogo_arboles.html',datos)


def catalogo_arbusto (request):
    producto = Producto.objects.filter(categoria = 5)

    datos = {
        'producto' : producto
        }
    return render(request, 'Catalogo_arbusto.html',datos)



def catalogo_flores (request):
    producto = Producto.objects.filter(categoria = 3)

    datos = {
        'producto' : producto
        }
    return render(request, 'Catalogo_flores.html',datos)

def catalogo_macetero (request):
    producto = Producto.objects.filter(categoria = 2)

    datos = {
        'producto' : producto
        }
    return render(request, 'Catalogo_macetero.html',datos)

def catalogo_herramientas (request):
    producto = Producto.objects.filter(categoria = 6)

    datos = {
        'producto' : producto
        }
    return render(request, 'Catalogo_herramientas.html',datos)




