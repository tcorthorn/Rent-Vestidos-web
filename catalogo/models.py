from logging import PlaceHolder

from pickle import TRUE

from trace import Trace
from venv import create
from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


#from catalogo.admin import VestidoAdmin #Used to generate URLs by reversing the URL patterns

class Categoria(models.Model):
    nombre= models.CharField(max_length=100, help_text="Ingrese el nombre de la Categoría (p. ej. Noche, Largo, Corto, Fiesta etc.)")
    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        """         Devuelve el URL a una instancia particular de Vestido         """
        return reverse('detalle-categoria', args=[str(self.id)])

    class Meta:
        ordering = ['nombre']

class Talla(models.Model):
    talla = models.CharField(max_length=100, help_text="Ingrese la talla")
    def __str__(self):
        return self.talla

    def get_absolute_url(self):
        """         Devuelve el URL a una instancia particular de Vestido         """
        return reverse('detalle-talla', args=[str(self.id)]) 

    class Meta:
        ordering = ['talla']  

class Vestido(models.Model):

    # ForeignKey, ya que un vestido tiene un solo proveedor, pero el mismo proveedor puede haber confeccionado muchos tipos de vestidos.
    # 'Proveedor' es un string, en vez de un objeto, porque la clase Proveedor aún no ha sido declarada.

    sku = models.CharField(unique=True, max_length=4, help_text="Sku único para este vestido particular en toda la tienda: Máximo 4 dígitos")
    nombre= models.CharField(max_length=200, help_text="Nombre que identifique el vestido fácilmente")
    detalle = models.CharField(max_length=1000, help_text="Ingrese una descripción del vestido")
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null= True, help_text="Seleccione una categoría para este vestido")
    talla = models.ForeignKey(Talla, on_delete=models.SET_NULL, null=True ,help_text="Seleccione una talla para este vestido")
    proveedor = models.ForeignKey('Proveedor',on_delete=models.SET_NULL, null=True ,default='Otro' , help_text="Opcional")
    LOAN_STATUS = (
        ('mantencion', 'Mantención'),
        ('arrendado', 'Arrendado'),
        ('disponible', 'Disponible'),
        #('reservado', 'Reservado'),
    )
    status = models.CharField(max_length=15, choices=LOAN_STATUS, blank=True, default='mantencion', help_text='Disponibilidad del vestido')

    LOAN_RESERVA = (
        ('Reservado', 'Reservado'),
        ('Sin reserva', 'No reservado'),
    )
    reservado = models.CharField(max_length=15, choices=LOAN_RESERVA, blank=True, default='Sin reserva', help_text='Disponibilidad del vestido')
    fecha_reservada = models.DateField(null=True,blank=True)
    cliente = models.ForeignKey('Cliente', on_delete=models.SET_NULL, null= True)

    # ManyToManyField, porque una categoria puede contener muchos vestidos y un vestido puede cubrir varias categorías.
    # La clase Categoria ya ha sido definida, entonces podemos especificar el objeto arriba.

    def __str__(self):
        return self.sku
    
    def get_absolute_url(self):
        """         Devuelve el URL a una instancia particular de Vestido         """
        return reverse('detalle-vestido', args=[str(self.id)])

    def display_categoria(self):
        """"         Creates a string for the Categoría. This is required to display categoria in Admin.        """
        return ', '.join([ categoria.nombre for categoria in self.categoria.all()[:3] ])
    display_categoria.short_description = 'Categoria'

    def display_talla(self):
        """"         Creates a string for the Talla. This is required to display talla in Admin.        """
        return ', '.join([ talla.talla for talla in self.talla.all()[:3] ])
    display_talla.short_description = 'Talla'


    class Meta:
        ordering = ['sku']


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100, default='Otro', help_text='Ingrese nombre y apellido de quien confeccionó el vestido')
    email = models.EmailField(null=True,blank=True, help_text='Opcional')
    telefono = models.CharField(max_length=10,null=True,blank=True , help_text='Opcional')

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un proveedor.
        """
        return reverse('detalle-proveedor', args=[str(self.id)])

    class Meta():
        verbose_name='proveedor'
        verbose_name_plural ='Proveedores'

class Cliente(models.Model):
    """
    Modelo que representa un cliente
    """
    nombre = models.CharField(max_length=100)
    apellidos= models.CharField(max_length=100)
    rut =models.CharField(unique=True, max_length=11, help_text='Ingrese RUT sin puntos y con digito verificador', default="12875587-9")
    email = models.EmailField()
    telefono = models.CharField(max_length=10)

    def get_absolute_url(self):
        """  Retorna la url para acceder a una instancia particular de un cliente.   """

        return reverse('detalle-cliente', args=[str(self.id)])

    def __str__(self):
        return self.nombre

    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
        return '%s %s' % (self.nombre, self.apellidos)

    class Meta:
        ordering = ['apellidos']
   
class Arriendo(models.Model):
    sku = models.ForeignKey('Vestido', help_text="VERIFIQUE el status del sku que identifica a este vestido particular", on_delete=models.SET_NULL, null=True)
    cliente = models.ManyToManyField('Cliente', help_text="Seleccione el cliente que arrienda")
    fecha_inicio= models.DateField(null=True, blank=True , help_text="Fecha inicio del arriendo")
    fecha_a_devolver = models.DateField(null=True, blank=True , help_text="Fecha que debe devolver el vestido")
    fecha_que_devolvio = models.DateField(null=True, blank=True , help_text="Fecha que devolvió el vestido")
    creado= models.DateTimeField(auto_now_add=True)
    modificado= models.DateTimeField(auto_now=True)
    comentario = models.CharField(max_length=500, null=True,blank=True)
    LOAN_STATUS = (
       #('mantencion', 'mantención'),
        #('arrendado', 'arrendado'),
        #('disponible', 'disponible'),
        ('reservado', 'reservado'),
        #('devuelto', 'devuelto'),
    )
    status = models.CharField(max_length=15, choices=LOAN_STATUS, blank=True, default='mantencion', help_text='Disponibilidad del vestido')
    
    
    #def get_absolute_url(self):
    """         Devuelve el URL a una instancia particular de Arriendo         """
        #return reverse('arriendo_create', args=[str(self.id)])

    @property
    def is_overdue(self):
        if self.fecha_a_devolver and date.today() > self.fecha_a_devolver:
            return True
        return False

    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un cliente.
        """
        return reverse('detalle-arriendos', args=[str(self.id)])

    def __str__(self):
        return self.sku

    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
        return '%s' % (self.cliente, )

    def display_cliente(self):
        """"         Creates a string for the cliente. This is required to display cliente in Admin.        """

        return ', '.join([ cliente.apellidos for cliente in self.cliente.all()[:3] ])
        
    display_cliente.short_description = 'Apellidos'

    def display_cliente2(self):
        """"         Creates a string for the cliente. This is required to display cliente in Admin.        """

        return ', '.join([ cliente.nombre for cliente in self.cliente.all()[:3] ])
        
    display_cliente2.short_description = 'Nombre'
    
    class Meta:
        ordering = ['-fecha_inicio']

class Reserva(models.Model):
    sku = models.ForeignKey(Vestido,on_delete=models.SET_NULL, null=True, help_text="Seleccione el cliente que reserva" )
    cliente = models.ManyToManyField(Cliente)
    fecha_reservada = models.DateField()
    #creado= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sku

    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
        return '%s' % (self.cliente, )

    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de una reserva.
        """
        return reverse('detalle-reservas', args=[str(self.id)])

    def display_cliente(self):
        """"         Creates a string for the cliente. This is required to display cliente in Admin.        """

        return ', '.join([ cliente.apellidos for cliente in self.cliente.all()[:3] ])
    display_cliente.short_description = 'Apellidos'

    def display_cliente2(self):
        """"         Creates a string for the cliente. This is required to display cliente in Admin.        """

        return ', '.join([ cliente.nombre for cliente in self.cliente.all()[:3] ])
    display_cliente2.short_description = 'Nombre'

    class Meta():
        verbose_name='reserva'
        verbose_name_plural ='reservas'

    class Meta:
        ordering = ['-fecha_reservada']
        

class Pago(models.Model):
    sku = models.ForeignKey(Vestido,on_delete=models.SET_NULL, null=True, help_text='Ingrese el Sku del vestido que reserva' )
    cliente = models.ManyToManyField (Cliente, help_text= "Ingrese cliente que pagó")
    monto_pagado = models.IntegerField(help_text="Ingrese el valor pagado")
    fecha_de_pago = models. DateField(help_text="Ingrese fecha de pago")
    comentario = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.sku

    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
        return '%s' % (self.cliente, )

    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de una reserva.
        """
        return reverse('detalle-reserva', args=[str(self.id)])

    def display_cliente(self):
        """"         Creates a string for the cliente. This is required to display cliente in Admin.        """

        return ', '.join([ cliente.apellidos for cliente in self.cliente.all()[:3] ])
    display_cliente.short_description = 'Apellidos'

    def display_cliente2(self):
        """"         Creates a string for the cliente. This is required to display cliente in Admin.        """

        return ', '.join([ cliente.nombre for cliente in self.cliente.all()[:3] ])
    display_cliente2.short_description = 'Nombre'

    class Meta():
        verbose_name='pago'
        verbose_name_plural ='pagos'
