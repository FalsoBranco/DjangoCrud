from django.db import models


class Genero(models.Model):

    genero = models.CharField("Genero", max_length=100)

    class meta:
        verbose_name = "Genero"
        verbose_name_plural = "Generos"

    def __str__(self):
        return self.genero


class Filme(models.Model):

    filme = models.CharField("Nome", max_length=100)
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT)
    quantidade = models.IntegerField("Quantidade", default=0)
    preco = models.DecimalField("Preço", decimal_places=2, max_digits=8)

    class meta:
        verbose_name = "Filme"
        verbose_name_plural = "Filmes"

    def __str__(self):
        return self.filme
