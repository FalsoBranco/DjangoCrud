from django.urls import path

from . import views

urlpatterns = [
    path("", views.FilmeListView.as_view(), name="index"),
    path("post/", views.movie_post, name="post"),
]
