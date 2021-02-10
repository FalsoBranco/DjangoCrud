from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView

from .form import FilmeForm
from .models import Filme


class FilmeListView(ListView):
    context_object_name = "filme_list"
    template_name = "filme/index.html"

    def get_queryset(self) -> QuerySet:
        return Filme.objects.all()


# Create your views here.


def movie_post(request: HttpRequest):
    if request.method == "POST":
        form = FilmeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("movie:index")

    form = FilmeForm()
    context = {}
    context["form"] = form
    return render(request, "filme/post.html", context)


def edit(request: HttpRequest, pk: int):
    post = get_object_or_404(Filme, pk=pk)
    form = FilmeForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect("movie:index")
    return render(request, "filme/edit.html", {"form": form})


def delete(request: HttpRequest, pk: int):
    post = get_object_or_404(Filme, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("movie:index")
    return render(request, "filme/delete.html", {"object": post})
