from django.urls import path

from . import views

urlpatterns = [
    path("", views.FilmeListView.as_view(), name="list"),
    path("<int:pk>/", views.FilmeDetailView.as_view(), name="detail"),
]
