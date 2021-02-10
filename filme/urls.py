from django.urls import path

from . import views

urlpatterns = [
    path("", views.filme_list, name="index"),
    path("filme_new/", views.filme_new, name="post"),
    path("filme_edit/<int:pk>/", views.filme_edit, name="edit"),
    path("filme_delete/<int:pk>/", views.filme_delete, name="delete"),
]
