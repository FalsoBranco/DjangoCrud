from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView

from .form import FilmeForm
from .models import Filme

# Create your views here.


def filme_list(request: HttpRequest):
    return render(request, "filme/filme_list.html", {"filmes": Filme.objects.all()})


def filme_new(request: HttpRequest):
    if request.method == "POST":
        form = FilmeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("filme:index")

    form = FilmeForm()
    context = {}
    context["form"] = form
    return render(request, "filme/filme_new.html", context)


def filme_edit(request: HttpRequest, pk: int):
    post = get_object_or_404(Filme, pk=pk)
    form = FilmeForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect("filme:index")
    return render(request, "filme/filme_edit.html", {"form": form})


def filme_delete(request: HttpRequest, pk: int):
    post = get_object_or_404(Filme, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("filme:index")
    return render(request, "filme/filme_delete.html", {"object": post})
