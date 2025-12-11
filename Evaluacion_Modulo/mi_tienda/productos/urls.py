from django.urls import path
from .views import ListaProductos, CrearProducto, EditarProducto, EliminarProducto

urlpatterns = [
    path('', ListaProductos.as_view(), name='lista_productos'),
    path('crear/', CrearProducto.as_view(), name='crear_producto'),
    path('editar/<int:pk>/', EditarProducto.as_view(), name='editar_producto'),
    path('eliminar/<int:pk>/', EliminarProducto.as_view(), name='eliminar_producto'),
]
