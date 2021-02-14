from rest_framework import serializers

from ..models import Filme


class FilmeSerializer(serializers.ModelSerializer):
    class meta:
        model = Filme
        fields = "__all__"
