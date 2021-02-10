from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.shortcuts import redirect, render
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
