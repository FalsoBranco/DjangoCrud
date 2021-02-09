from django.http import HttpRequest
from django.shortcuts import redirect, render

from .form import FilmeForm


# Create your views here.
def index(request: HttpRequest):
    return render(request, "filme/index.html")


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
