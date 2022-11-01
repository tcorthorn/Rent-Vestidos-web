from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),

    path('vestidos/', views.VestidoListView.as_view(), name='vestidos'),
    path('clientes/', views.ClienteListView.as_view(), name='clientes'),
    path('proveedores/', views.ProveedorListView.as_view(), name='proveedores'),
    path('reservas/', views.ReservaListView.as_view(), name='reservas'),
    path('arriendos/', views.ArriendoListView.as_view(), name='arriendos'),
    
    
    path('vestidos/<pk>', views.VestidoDetailView.as_view(), name='detalle-vestido'),
    path('clientes/<pk>', views.ClienteDetailView.as_view(), name='detalle-cliente'),
    path('proveedores/<pk>', views.ProveedorDetailView.as_view(), name='detalle-proveedor'),
    path('reservas/<pk>', views.ReservaDetailView.as_view(), name='detalle-reservas'),
    path('arriendos/<pk>', views.ArriendoDetailView.as_view(), name='detalle-arriendos'),

    path('arrendados/', views.ArrendadoListView.as_view(), name='arrendados'),
    path('disponibles/', views.DisponibleListView.as_view(), name='disponibles'),
    path('mantencion/', views.MantencionListView.as_view(), name='mantencion'),
    
]
   
urlpatterns += [
    path('cliente/create/', views.ClienteCreate.as_view(), name='cliente_create'),
    path('cliente/<pk>/update/', views.ClienteUpdate.as_view(), name='cliente_update'),
    path('cliente/<pk>/delete/', views.ClienteDelete.as_view(), name='cliente_delete'),
]
    

urlpatterns += [
    path('arriendo/create/', views.ArriendoCreate.as_view(), name='arriendo_create'),
    path('arriendo/(<pk>/update/', views.ArriendoUpdate.as_view(), name='arriendo_update'),
    path('arriendo/<pk>/delete/', views.ArriendoDelete.as_view(), name='arriendo_delete'),
]

urlpatterns += [
    path('vestido/create/', views.VestidoCreate.as_view(), name='vestido_create'),
    path('vestido/<pk>/update/', views.VestidoUpdate.as_view(), name='vestido_update'),
    path('vestido/<pk>/delete/', views.VestidoDelete.as_view(), name='vestido_delete'),
]

urlpatterns += [
    path('reserva/create/', views.ReservaCreate.as_view(), name='reserva_create'),
    path('reserva/(<pk>/update/', views.ReservaUpdate.as_view(), name='reserva_update'),
    path('reserva/<pk>/delete/', views.ReservaDelete.as_view(), name='reserva_delete'),
]

