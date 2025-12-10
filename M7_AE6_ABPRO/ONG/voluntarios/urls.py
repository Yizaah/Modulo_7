from django.urls import path
from . import views

urlpatterns = [
    # HOME
    path("", views.evento_list, name="home"),

    # VOLUNTARIOS
    path("voluntarios/", views.voluntario_list, name="voluntario_list"),
    path("voluntarios/nuevo/", views.voluntario_create, name="voluntario_create"),
    path("voluntarios/<int:pk>/editar/", views.voluntario_update, name="voluntario_update"),
    path("voluntarios/<int:pk>/eliminar/", views.voluntario_delete, name="voluntario_delete"),

    # EVENTOS
    path("eventos/", views.evento_list, name="evento_list"),
    path("eventos/nuevo/", views.evento_create, name="evento_create"),
    path("eventos/<int:pk>/editar/", views.evento_update, name="evento_update"),
    path("eventos/<int:pk>/eliminar/", views.evento_delete, name="evento_delete"),
]
