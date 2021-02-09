from django.contrib import admin

from filme.models import Filme, Genero

# Register your models here.


admin.site.register(Filme)
admin.site.register(Genero)
