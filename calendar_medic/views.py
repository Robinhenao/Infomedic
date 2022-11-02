from django.shortcuts import render, redirect
from django.contrib import messages
from calendar_medic.forms import form_paciente, form_acompanante, form_cita
from calendar_medic.models import Cita, Paciente, Acompanante
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
def agenda(request):
    listado_posts = Cita.objects.all()
    paginator = Paginator(listado_posts, 6)
    pagina = request.GET.get("page") or 1
    posts = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, posts.paginator.num_pages + 1)
    return render(request, "agenda.html", {"projects": posts, "paginas": paginas, "pagina_actual": pagina_actual})


def make_paciente(request):
    if request.method == "POST":
        form = form_paciente(request.POST, request.FILES)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.save()

            return redirect("make_acompanante")
        else:
            for msg in form.error_message:
                messages.error(request, form.error_messages[msg])
    form = form_paciente()
    return render(request, "make_formulario.html", {"form": form})


def make_acompanante(request):
    if request.method == "POST":
        form = form_acompanante(request.POST, request.FILES)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.save()
            return redirect("make_cita")
        else:
            for msg in form.error_message:
                messages.error(request, form.error_messages[msg])
    form = form_acompanante()
    return render(request, "make_formulario.html", {"form": form})


def make_cita(request):
    if request.method == "POST":
        form = form_cita(request.POST, request.FILES)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.author_id = request.user.id
            proyecto.save()
            return redirect("agenda")
        else:
            for msg in form.error_message:
                messages.error(request, form.error_messages[msg])
    form = form_cita()
    return render(request, "make_formulario.html", {"form": form})


def delete_cita(request, project_id):
    try:
        proyecto = Cita.objects.get(pk=project_id)
    except proyecto.DoesNotExist:
        messages.error(request, "la cita a eliminar no existe")
    proyecto.delete()
    return redirect("agenda")


def update_cita(request, project_id):
    project = Cita.objects.get(id=project_id)
    if request.method == "POST":
        form = form_cita(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect("agenda")
        else:
            for msg in form.error_message:
                messages.error(request, form.error_messages[msg])
    form = form_cita(instance=project)
    return render(request, "make_formulario.html", {"form": form})
