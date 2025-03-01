from django.contrib import admin

from django.contrib import admin

from .models import Evento, Boleto, Localidad, Noticia
admin.site.register(Evento)
admin.site.register(Boleto) 
admin.site.register(Localidad)
admin.site.register(Noticia)


