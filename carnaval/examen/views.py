from django.shortcuts import render
from .models import Evento, Producto, Boleto,Noticia

def index(request):
    noticias = Noticia.objects.all()  # Recuperamos todas las noticias
    eventos = Evento.objects.all()    # Recuperamos todos los eventos
    return render(request, 'index.html', {'noticias': noticias, 'eventos': eventos})


def eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos.html', {'eventos': eventos})

def boletos(request):
    boletos = Boleto.objects.all()
    return render(request, 'boletos.html', {'boletos': boletos})

