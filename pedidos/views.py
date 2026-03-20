from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Cliente, Restaurante, Repartidor, Pedido
from .forms import ClienteForm, RestauranteForm, RepartidorForm, PedidoForm

#Home / pag Principal
def home(request):
    return render(request, 'pedidos/home.html')

#vistas de prueba
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'pedidos/lista_clientes.html', {'clientes': clientes})

def lista_restaurantes(request):
    restaurantes = Restaurante.objects.all()
    return render(request, 'pedidos/lista_restaurantes.html', {'restaurantes': restaurantes})

def lista_repartidores(request):
    repartidores = Repartidor.objects.all()
    return render(request, 'pedidos/lista_repartidores.html', {'repartidores': repartidores})

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/lista_pedidos.html', {'pedidos': pedidos})

# REGISTRAR
def registrar_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Cliente registrado correctamente.')
        return redirect('registrar_cliente')
    return render(request, 'pedidos/registrar.html', {'form': form, 'titulo': 'Registrar Cliente'})

def registrar_restaurante(request):
    form = RestauranteForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Restaurante registrado correctamente.')
        return redirect('registrar_restaurante')
    return render(request, 'pedidos/registrar.html', {'form': form, 'titulo': 'Registrar Restaurante'})

def registrar_repartidor(request):
    form = RepartidorForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Repartidor registrado correctamente.')
        return redirect('registrar_repartidor')
    return render(request, 'pedidos/registrar.html', {'form': form, 'titulo': 'Registrar Repartidor'})

def registrar_pedido(request):
    form = PedidoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Pedido registrado correctamente.')
        return redirect('registrar_pedido')
    return render(request, 'pedidos/registrar.html', {'form': form, 'titulo': 'Registrar Pedido'})


# EDITAR
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        messages.success(request, 'Cliente actualizado correctamente.')
        return redirect('editar_cliente', pk=pk)
    return render(request, 'pedidos/editar.html', {'form': form, 'titulo': 'Editar Cliente', 'objeto': cliente})

def editar_restaurante(request, pk):
    restaurante = get_object_or_404(Restaurante, pk=pk)
    form = RestauranteForm(request.POST or None, instance=restaurante)
    if form.is_valid():
        form.save()
        messages.success(request, 'Restaurante actualizado correctamente.')
        return redirect('editar_restaurante', pk=pk)
    return render(request, 'pedidos/editar.html', {'form': form, 'titulo': 'Editar Restaurante', 'objeto': restaurante})

def editar_repartidor(request, pk):
    repartidor = get_object_or_404(Repartidor, pk=pk)
    form = RepartidorForm(request.POST or None, instance=repartidor)
    if form.is_valid():
        form.save()
        messages.success(request, 'Repartidor actualizado correctamente.')
        return redirect('editar_repartidor', pk=pk)
    return render(request, 'pedidos/editar.html', {'form': form, 'titulo': 'Editar Repartidor', 'objeto': repartidor})

def editar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    form = PedidoForm(request.POST or None, instance=pedido)
    if form.is_valid():
        form.save()
        messages.success(request, 'Pedido actualizado correctamente.')
        return redirect('editar_pedido', pk=pk)
    return render(request, 'pedidos/editar.html', {'form': form, 'titulo': 'Editar Pedido', 'objeto': pedido})


# STATUS 

def cambiar_status(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        nuevo_status = request.POST.get('status')
        pedido.status = nuevo_status
        pedido.save()
        messages.success(request, f'Estado del pedido #{pedido.pk} actualizado a {pedido.get_status_display()}.')
        return redirect('lista_pedidos')
    
    return render(request, 'pedidos/status.html', {'pedido': pedido})


# PROPINAS
def gestionar_propina(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        nueva_propina = request.POST.get('propina')
        pedido.propina = nueva_propina
        pedido.save()
        messages.success(request, f'Propina del {nueva_propina}% aplicada al pedido #{pedido.pk}.')
        return redirect('editar_pedido', pk=pk)
    
    return render(request, 'pedidos/propinas.html', {'pedido': pedido})


# ELIMINAR 
def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'Cliente eliminado correctamente.')
        # Redirigimos a registrar porque no veo una vista de "lista", pero puedes cambiarlo a tu gusto
        return redirect('registrar_cliente') 
    return render(request, 'pedidos/eliminar.html', {'titulo': 'Eliminar Cliente', 'objeto': cliente})

def eliminar_restaurante(request, pk):
    restaurante = get_object_or_404(Restaurante, pk=pk)
    if request.method == 'POST':
        restaurante.delete()
        messages.success(request, 'Restaurante eliminado correctamente.')
        return redirect('registrar_restaurante')
    return render(request, 'pedidos/eliminar.html', {'titulo': 'Eliminar Restaurante', 'objeto': restaurante})

def eliminar_repartidor(request, pk):
    repartidor = get_object_or_404(Repartidor, pk=pk)
    if request.method == 'POST':
        repartidor.delete()
        messages.success(request, 'Repartidor eliminado correctamente.')
        return redirect('registrar_repartidor')
    return render(request, 'pedidos/eliminar.html', {'titulo': 'Eliminar Repartidor', 'objeto': repartidor})

def eliminar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        pedido.delete()
        messages.success(request, 'Pedido eliminado correctamente.')
        return redirect('registrar_pedido')
    return render(request, 'pedidos/eliminar.html', {'titulo': 'Eliminar Pedido', 'objeto': pedido})


# RATING
def rating_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        nuevo_rating = request.POST.get('rating')
        if nuevo_rating:
            cliente.rating = int(nuevo_rating)
            cliente.save()
            messages.success(request, 'Calificación del cliente guardada.')
            return redirect('lista_clientes')
    return render(request, 'pedidos/rating.html', {'titulo': 'Calificar Cliente', 'objeto': cliente})

def rating_restaurante(request, pk):
    restaurante = get_object_or_404(Restaurante, pk=pk)
    if request.method == 'POST':
        nuevo_rating = request.POST.get('rating')
        if nuevo_rating:
            restaurante.rating = int(nuevo_rating)
            restaurante.save()
            messages.success(request, 'Calificación del restaurante guardada.')
            return redirect('lista_restaurantes')
    return render(request, 'pedidos/rating.html', {'titulo': 'Calificar Restaurante', 'objeto': restaurante})

def rating_repartidor(request, pk):
    repartidor = get_object_or_404(Repartidor, pk=pk)
    if request.method == 'POST':
        nuevo_rating = request.POST.get('rating')
        if nuevo_rating:
            repartidor.rating = int(nuevo_rating)
            repartidor.save()
            messages.success(request, 'Calificación del repartidor guardada.')
            return redirect('lista_repartidores')
    return render(request, 'pedidos/rating.html', {'titulo': 'Calificar Repartidor', 'objeto': repartidor})