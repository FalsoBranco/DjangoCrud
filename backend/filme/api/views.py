from rest_framework.generics import ListAPIView, RetrieveAPIView

from ..models import Filme
from .serializers import FilmeSerializer


class FilmeListView(ListAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer


class FilmeDetailView(RetrieveAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
