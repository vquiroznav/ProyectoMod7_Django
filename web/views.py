from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario

def inicio(request):
    return render(request, 'inicio.html')

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/lista.html', {'usuarios': usuarios})

def crear_usuario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        saldo = request.POST['saldo']
        Usuario.objects.create(nombre=nombre, email=email, saldo=saldo)
        return redirect('lista_usuarios')
    return render(request, 'usuarios/form.html')

def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        usuario.nombre = request.POST['nombre']
        usuario.email = request.POST['email']
        usuario.saldo = request.POST['saldo']
        usuario.save()
        return redirect('lista_usuarios')
    return render(request, 'usuarios/form.html', {'usuario': usuario})

def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.delete()
    return redirect('lista_usuarios')
