from django.shortcuts import render, redirect
from .models import Pedido
from .forms import pedidoForm, clienteForm
from .models import Cliente


def pedido(request):
    pedidos = Pedido.objects.all()
    ctx={
        'pedidos' : pedidos,
    }
    return render(request, 'pedido.html', ctx)

def createpedido(request):
    if request.method == 'GET':
        form = pedidoForm()
        ctx = {
            'form': form
        }
    else:
        form = pedidoForm(request.POST)
        ctx = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('pedidos')

    return render(request, 'manage_pedidos.html', ctx)

def cliente(request):
    clientes = Cliente.objects.all()
    ctx={
        'clientes': clientes,
    }
    return render(request, 'cliente.html', ctx)

def createcliente(request):
    if request.method == 'GET':
        form = clienteForm()
        ctx = {
            'form': form
        }
    else:
        form = clienteForm(request.POST)
        ctx = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('cliente_usuario')

    return render(request, 'manage_cliente.html', ctx)
    
 