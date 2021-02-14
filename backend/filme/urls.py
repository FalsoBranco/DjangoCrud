from django.urls import path

from . import views

urlpatterns = [
    path("", views.FilmeListView.as_view(), name="index"),
    path("post/", views.movie_post, name="post"),
    path("edit/<int:pk>/", views.edit, name="edit"),
    path("delete/<int:pk>/", views.delete, name="delete"),
]
