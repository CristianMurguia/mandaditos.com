from django.urls import path
from . import views

urlpatterns = [

    #Home pag Principal
    path('', views.home, name='home'),

    #pruebas
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('restaurantes/', views.lista_restaurantes, name='lista_restaurantes'),
    path('repartidores/', views.lista_repartidores, name='lista_repartidores'),
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),

    # REGISTRAR
    path('clientes/nuevo/',      views.registrar_cliente,     name='registrar_cliente'),
    path('restaurantes/nuevo/',  views.registrar_restaurante, name='registrar_restaurante'),
    path('repartidores/nuevo/',  views.registrar_repartidor,  name='registrar_repartidor'),
    path('pedidos/nuevo/',       views.registrar_pedido,      name='registrar_pedido'),

    # EDITAR
    path('clientes/<int:pk>/editar/',     views.editar_cliente,     name='editar_cliente'),
    path('restaurantes/<int:pk>/editar/', views.editar_restaurante, name='editar_restaurante'),
    path('repartidores/<int:pk>/editar/', views.editar_repartidor,  name='editar_repartidor'),
    path('pedidos/<int:pk>/editar/',      views.editar_pedido,      name='editar_pedido'),

    # STATUS
    path('pedidos/<int:pk>/status/', views.cambiar_status, name='cambiar_status'),

    # PROPINAS
    path('pedidos/<int:pk>/propina/', views.gestionar_propina, name='gestionar_propina'),

   # --- RUTAS PARA ELIMINAR ---
    path('clientes/<int:pk>/eliminar/', views.eliminar_cliente, name='eliminar_cliente'),
    path('restaurantes/<int:pk>/eliminar/', views.eliminar_restaurante, name='eliminar_restaurante'),
    path('repartidores/<int:pk>/eliminar/', views.eliminar_repartidor, name='eliminar_repartidor'),
    path('pedidos/<int:pk>/eliminar/', views.eliminar_pedido, name='eliminar_pedido'),

    # --- RUTAS PARA RATING ---
    path('rating/cliente/<int:pk>/', views.rating_cliente, name='rating_cliente'),
    path('rating/restaurante/<int:pk>/', views.rating_restaurante, name='rating_restaurante'),
    path('rating/repartidor/<int:pk>/', views.rating_repartidor, name='rating_repartidor'),
]