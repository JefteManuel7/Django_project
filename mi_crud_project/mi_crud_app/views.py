
# Create your views here.
# mi_crud_app/views.py
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Producto
from .forms import ProductoForm
from django.utils import timezone

class ListaProductosView(ListView):
    model = Producto
    template_name = 'mi_crud_app/lista_productos.html'
    context_object_name = 'productos'

class AgregarProductoView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'mi_crud_app/agregar_producto.html'
    success_url = reverse_lazy('lista_productos')

    def form_valid(self, form):
        form.instance.fecha_creacion = timezone.now()  # Asigna la fecha actual al campo fecha_creacion
        return super().form_valid(form)


class EditarProductoView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'mi_crud_app/editar_producto.html'
    success_url = reverse_lazy('lista_productos')

    def get_object(self, queryset=None):
        # Accede al valor de producto_id desde la URL
        producto_id = self.kwargs['pk']
        # Utiliza producto_id para buscar el objeto Producto en la base de datos
        return Producto.objects.get(pk=producto_id)
        
    


class EliminarProductoView(DeleteView):
    model = Producto
    template_name = 'mi_crud_app/eliminar_producto.html'
    success_url = reverse_lazy('lista_productos')

class DetalleProductoView(DetailView):
    model = Producto
    template_name = 'mi_crud_app/detalle_producto.html'
    context_object_name = 'producto'


def home(request):
    return render(request, 'mi_crud_app/home.html')