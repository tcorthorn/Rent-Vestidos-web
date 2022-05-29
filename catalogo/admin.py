from django.contrib import admin
from .models import Arriendo, Proveedor, Categoria, Reserva, Vestido, Cliente,Talla, Reserva, Pago
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from datetime import date

class GastosResource(resources.ModelResource):
    class Meta:
        model = Proveedor
        model = Cliente
        model = Categoria
        model = Talla
        model = Vestido
        model = Arriendo
        model = Reserva
        model= Pago

# Define the admin class
class ProveedorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono')
    resources_class=Proveedor
    search_fields=("nombre", )
    
# Register the admin class with the associated model
admin.site.register(Proveedor, ProveedorAdmin)

@admin.register(Cliente)
class ClienteAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('nombre','apellidos','rut', 'email', 'telefono')
    list_filter = ('apellidos', 'nombre')
    resources_class=Cliente
    search_fields=("nombre", )

@admin.register(Categoria)
class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('nombre',)
    resources_class=Categoria
    search_fields=("nombre", )

@admin.register(Talla)
class TallaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('talla',)
    resources_class=Talla
    search_fields=("nombre", )

class ReservaInline(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""
    model = Reserva
    extra= 0

@admin.register(Vestido)
class VestidoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ( 'sku','status','reservado','nombre','talla', 'categoria','proveedor' )
    list_filter = ('status','talla','categoria')
    resources_class=Vestido
    search_fields=('fecha_a_devolver', )
    inlines = [ReservaInline]

@admin.register(Arriendo)
class ArriendoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('sku','display_cliente','display_cliente2','fecha_inicio','fecha_a_devolver','fecha_que_devolvio','creado', 'modificado','comentario')
    fields = ['sku','cliente', ('fecha_inicio', 'fecha_a_devolver','fecha_que_devolvio'),'comentario']
    list_filter = ('sku',)
    resources_class=Arriendo
    search_fields=("sku", )

@admin.register(Reserva)
class ReservaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('sku','display_cliente','display_cliente2','fecha_reservada')
    fields = ['sku', 'cliente','fecha_reservada' ]
    list_filter = ('fecha_reservada','sku', )
    resources_class=Reserva
    search_fields=( 'fecha_reservada',"sku" )
    
@admin.register(Pago)
class PagoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('sku','display_cliente','display_cliente2','fecha_de_pago')
    #fields = ['sku', 'cliente','fecha_de_pago' ]
    list_filter = ('fecha_de_pago','sku', )
    resources_class=Pago
    search_fields=( 'fecha_de_pago',"sku" )

