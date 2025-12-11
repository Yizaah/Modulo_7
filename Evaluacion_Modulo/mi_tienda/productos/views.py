from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Producto
from .forms import ProductoForm

class ListaProductos(ListView):
    model = Producto
    template_name = "productos/lista_productos.html"
    context_object_name = "productos"


class CrearProducto(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = "productos/crear_producto.html"
    success_url = reverse_lazy('lista_productos')


class EditarProducto(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = "productos/editar_producto.html"
    success_url = reverse_lazy('lista_productos')


class EliminarProducto(DeleteView):
    model = Producto
    template_name = "productos/eliminar_producto.html"
    success_url = reverse_lazy('lista_productos')
