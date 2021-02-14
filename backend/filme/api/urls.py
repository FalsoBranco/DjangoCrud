from django.urls import path

from .views import FilmeDetailView, FilmeListView

urlpatterns = [
    path("", FilmeListView.as_view()),
]
