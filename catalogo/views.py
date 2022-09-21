from django.shortcuts import render
from catalogo.forms import ReservaForm
from .models import Proveedor, Categoria, Vestido,  Cliente, Arriendo, Reserva
from django.views import generic
from datetime import date
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    vestidos=Vestido.objects.all().count()
    clientes=Cliente.objects.all().count()
    proveedores=Proveedor.objects.all().count()

    vestidos_disponibles=Vestido.objects.filter(status='disponible').count()
    vestidos_arrendados=Vestido.objects.filter(status='arrendado').count()
    vestidos_mantencion=Vestido.objects.filter(status='mantencion').count()
    vestidos_reservados=Vestido.objects.filter(reservado='Reservado').count()

    num_visitas = request.session.get('num_visitas', 0)
    request.session['num_visitas'] = num_visitas + 1

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={
        'vestidos':vestidos,
        'clientes':clientes,
        'proveedores':proveedores,
        'vestidos_disponibles':vestidos_disponibles, 
        'vestidos_arrendados':vestidos_arrendados,
        'vestidos_mantencion':vestidos_mantencion,
        'vestidos_reservados':vestidos_reservados,
        'num_visitas':num_visitas,
        }
    )

class VestidoListView(generic.ListView):
    model = Vestido
    paginate_by = 10

class ClienteListView(generic.ListView):
    model = Cliente
    paginate_by = 10 

class ProveedorListView(generic.ListView):
    model = Proveedor
    paginate_by = 10

class ReservaListView(generic.ListView):
    model = Reserva
    paginate_by = 10

class ArriendoListView(generic.ListView):
    model = Arriendo
    paginate_by = 10

# Detalle de la Clase

class VestidoDetailView(generic.DetailView):
    model = Vestido
    paginate_by = 10

class ClienteDetailView(generic.DetailView):
    model = Cliente
    paginate_by = 10

class ProveedorDetailView(generic.DetailView):
    model = Proveedor
    paginate_by = 10

class ReservaDetailView(generic.DetailView):
    model = Reserva
    paginate_by = 10

class ArriendoDetailView(generic.DetailView):
    model = Arriendo
    paginate_by = 10
    
    #Listas genericas de status de la clase Vestido

class ArrendadoListView(generic.ListView):
    model = Vestido
    paginate_by = 10
    queryset = Vestido.objects.filter(status__icontains='arrendado') #vestidos arrendados
    template_name = 'Arriendo/arriendo_list.html'  # Specify your own template name/location

class DisponibleListView(generic.ListView):
    model = Vestido
    paginate_by = 10
    queryset = Vestido.objects.filter(status__icontains='disponible') #vestidos disponibles
    template_name = 'Vestido/disponible_list.html'  # Specify your own template name/location

class MantencionListView(generic.ListView):
    model = Vestido
    paginate_by = 10
    queryset = Vestido.objects.filter(status__icontains='mantencion') #vestidos mantencion
    template_name = 'Vestido/mantencion_list.html'  # Specify your own template name/location

#CRUD

class ClienteCreate(CreateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('clientes')
    
class ClienteUpdate(UpdateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('clientes')

class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes')
    fields = '__all__'


class ArriendoCreate(CreateView):
    model = Arriendo
    fields = ['sku','cliente','fecha_inicio','fecha_a_devolver','fecha_que_devolvio','comentario']
    success_url = reverse_lazy('vestidos')

class ArriendoUpdate(UpdateView):
    model = Arriendo
    fields = '__all__'
    success_url = reverse_lazy('vestidos')

class ArriendoDelete(DeleteView):
    model = Arriendo
    success_url = reverse_lazy('vestidos')

class VestidoCreate(CreateView):
    model = Vestido
    fields = ['sku','status']
    success_url = reverse_lazy('vestidos')

class VestidoUpdate(UpdateView):
    model = Vestido
    fields = ['status','reservado','fecha_reservada']
    success_url = reverse_lazy('vestidos')

class VestidoDelete(DeleteView):
    model = Vestido
    success_url = reverse_lazy('vestidos')

class ReservaCreate(CreateView):
    model = Reserva
    #form_class = ReservaForm
    fields = '__all__'
    success_url = reverse_lazy('vestidos')

class ReservaUpdate(UpdateView):
    model = Reserva
    fields = '__all__'
    success_url = reverse_lazy('vestidos')

class ReservaDelete(DeleteView):
    model = Reserva
    success_url = reverse_lazy('vestidos')

