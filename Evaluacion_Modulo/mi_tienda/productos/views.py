from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Producto
from .forms import ProductoForm
from django.views.generic import DetailView
from django.views.generic import ListView as DjangoListView
from django.views.generic import CreateView as DjangoCreateView, UpdateView as DjangoUpdateView, DeleteView as DjangoDeleteView
from .models import Categoria, Etiqueta
from django.urls import reverse_lazy


class ProductoDetalle(DetailView):
    model = Producto
    template_name = 'productos/detalle.html'
    context_object_name = 'producto'


# Categorias
class ListaCategorias(DjangoListView):
    model = Categoria
    template_name = 'categorias/lista.html'
    context_object_name = 'categorias'


class CrearCategoria(LoginRequiredMixin, DjangoCreateView):
    login_url = '/accounts/login/'
    model = Categoria
    fields = ['nombre', 'descripcion']
    template_name = 'categorias/formulario.html'
    success_url = reverse_lazy('lista_categorias')


class EditarCategoria(LoginRequiredMixin, DjangoUpdateView):
    login_url = '/accounts/login/'
    model = Categoria
    fields = ['nombre', 'descripcion']
    template_name = 'categorias/formulario.html'
    success_url = reverse_lazy('lista_categorias')


class EliminarCategoria(LoginRequiredMixin, DjangoDeleteView):
    login_url = '/accounts/login/'
    model = Categoria
    template_name = 'categorias/eliminar.html'
    success_url = reverse_lazy('lista_categorias')


# Etiquetas
class ListaEtiquetas(DjangoListView):
    model = Etiqueta
    template_name = 'etiquetas/lista.html'
    context_object_name = 'etiquetas'


class CrearEtiqueta(LoginRequiredMixin, DjangoCreateView):
    login_url = '/accounts/login/'
    model = Etiqueta
    fields = ['nombre']
    template_name = 'etiquetas/formulario.html'
    success_url = reverse_lazy('lista_etiquetas')


class EditarEtiqueta(LoginRequiredMixin, DjangoUpdateView):
    login_url = '/accounts/login/'
    model = Etiqueta
    fields = ['nombre']
    template_name = 'etiquetas/formulario.html'
    success_url = reverse_lazy('lista_etiquetas')


class EliminarEtiqueta(LoginRequiredMixin, DjangoDeleteView):
    login_url = '/accounts/login/'
    model = Etiqueta
    template_name = 'etiquetas/eliminar.html'
    success_url = reverse_lazy('lista_etiquetas')


class ListaProductos(ListView):
    model = Producto
    template_name = "productos/lista.html"
    context_object_name = "productos"


class CrearProducto(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    model = Producto
    form_class = ProductoForm
    template_name = "productos/crear.html"
    success_url = reverse_lazy('lista_productos')


class EditarProducto(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    model = Producto
    form_class = ProductoForm
    template_name = "productos/editar.html"
    success_url = reverse_lazy('lista_productos')


class EliminarProducto(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    model = Producto
    template_name = "productos/eliminar.html"
    success_url = reverse_lazy('lista_productos')
