from django.shortcuts import render, get_object_or_404, redirect
from .models import Voluntario, Evento
from .forms import VoluntarioForm, EventoForm


# -----------------------
# VOLUNTARIOS
# -----------------------

def voluntario_list(request):
    voluntarios = Voluntario.objects.all()
    return render(request, "voluntarios/voluntario_list.html", {"voluntarios": voluntarios})

def voluntario_create(request):
    if request.method == "POST":
        form = VoluntarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("voluntario_list")
    else:
        form = VoluntarioForm()

    return render(request, "voluntarios/voluntario_form.html", {"form": form})


def voluntario_update(request, pk):
    try:
        voluntario = Voluntario.objects.get(id=pk)
    except Voluntario.DoesNotExist:
        return redirect("voluntario_list")

    if request.method == "POST":
        form = VoluntarioForm(request.POST, instance=voluntario)
        if form.is_valid():
            form.save()
            return redirect("voluntario_list")
    else:
        form = VoluntarioForm(instance=voluntario)

    return render(request, "voluntarios/voluntario_form.html", {"form": form})

def voluntario_delete(request, pk):
    voluntario = get_object_or_404(Voluntario, pk=pk)

    if request.method == "POST":
        voluntario.delete()
        return redirect("voluntario_list")

    return render(request, "voluntarios/voluntario_confirm_delete.html", {"voluntario": voluntario})


# -----------------------
# EVENTOS
# -----------------------

def evento_list(request):
    eventos = Evento.objects.all()
    return render(request, "voluntarios/evento_list.html", {"eventos": eventos})

def evento_create(request):
    if request.method == "POST":
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("evento_list")
    else:
        form = EventoForm()

    return render(request, "voluntarios/evento_form.html", {"form": form})


def evento_update(request, pk):
    try:
        evento = Evento.objects.get(id=pk)
    except Evento.DoesNotExist:
        return redirect("evento_list")

    if request.method == "POST":
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect("evento_list")
    else:
        form = EventoForm(instance=evento)

    return render(request, "voluntarios/evento_form.html", {"form": form})

def evento_delete(request, pk):
    evento = get_object_or_404(Evento, pk=pk)

    if request.method == "POST":
        evento.delete()
        return redirect("evento_list")

    return render(request, "voluntarios/evento_confirm_delete.html", {"evento": evento})
