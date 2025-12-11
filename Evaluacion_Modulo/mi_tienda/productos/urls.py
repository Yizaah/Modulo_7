from django.urls import path
from .views import (
    ListaProductos,
    CrearProducto,
    EditarProducto,
    EliminarProducto,
    ProductoDetalle,
    ListaCategorias,
    CrearCategoria,
    EditarCategoria,
    EliminarCategoria,
    ListaEtiquetas,
    CrearEtiqueta,
    EditarEtiqueta,
    EliminarEtiqueta,
)

urlpatterns = [
    path('', ListaProductos.as_view(), name='lista_productos'),
    path('crear/', CrearProducto.as_view(), name='crear_producto'),
    path('<int:pk>/', ProductoDetalle.as_view(), name='detalle_producto'),
    path('editar/<int:pk>/', EditarProducto.as_view(), name='editar_producto'),
    path('eliminar/<int:pk>/', EliminarProducto.as_view(), name='eliminar_producto'),

    # Categorias
    path('categorias/', ListaCategorias.as_view(), name='lista_categorias'),
    path('categorias/crear/', CrearCategoria.as_view(), name='crear_categoria'),
    path('categorias/editar/<int:pk>/', EditarCategoria.as_view(), name='editar_categoria'),
    path('categorias/eliminar/<int:pk>/', EliminarCategoria.as_view(), name='eliminar_categoria'),

    # Etiquetas
    path('etiquetas/', ListaEtiquetas.as_view(), name='lista_etiquetas'),
    path('etiquetas/crear/', CrearEtiqueta.as_view(), name='crear_etiqueta'),
    path('etiquetas/editar/<int:pk>/', EditarEtiqueta.as_view(), name='editar_etiqueta'),
    path('etiquetas/eliminar/<int:pk>/', EliminarEtiqueta.as_view(), name='eliminar_etiqueta'),
]
