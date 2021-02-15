from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("", views.FilmeListView, basename="list")
# router.register("<int:pk>/", views.FilmeDetailView, basename="detail")

urlpatterns = [
    path("", include(router.urls)),
]
