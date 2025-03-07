from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento, Boleto,Noticia, Localidad
from django.utils import timezone
from django.http import JsonResponse
from django.utils.dateparse import parse_datetime
from django.views.decorators.http import require_http_methods


from django.utils.timezone import make_aware
from django.contrib.auth.decorators import login_required


from django.contrib.auth.decorators import login_required

def ver_boletos(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    boletos = Boleto.objects.filter(evento=evento)

    return render(request, 'boletos.html', {
        'evento': evento,
        'boletos': boletos,
    })

@login_required
def crear_boleto(request):
    eventos = Evento.objects.all()
    

    for evento in eventos:
        evento.localidades_data = f"localidades_{evento.id}"  
    
    return render(request, 'productos.html', {'eventos': eventos})

@login_required
def eliminar_boleto(request, boleto_id):
    if request.method == 'POST':
       
        boleto = get_object_or_404(Boleto, id=boleto_id)

       
        boleto.delete()

        return JsonResponse({'message': 'Boleto eliminado correctamente'}, status=200)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

def agregar_evento(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        localidad_id = request.POST.get('localidad')

        if not name or not fecha_inicio or not fecha_fin or not localidad_id:
            return JsonResponse({'error': 'Todos los campos son obligatorios'}, status=400)

        fecha_inicio_dt = timezone.datetime.strptime(fecha_inicio, '%Y-%m-%dT%H:%M')
        fecha_inicio_dt = timezone.make_aware(fecha_inicio_dt)

        fecha_fin_dt = timezone.datetime.strptime(fecha_fin, '%Y-%m-%dT%H:%M')
        fecha_fin_dt = timezone.make_aware(fecha_fin_dt)

        if fecha_inicio_dt < timezone.now():
            return JsonResponse({'error': 'La fecha de inicio no puede ser menor a la fecha actual'}, status=400)

        if fecha_fin_dt < fecha_inicio_dt:
            return JsonResponse({'error': 'La fecha de fin no puede ser menor a la de inicio'}, status=400)

        localidad = Localidad.objects.get(id=localidad_id)

        evento = Evento.objects.create(
            name=name,
            fecha_inicio=fecha_inicio_dt,
            fecha_fin=fecha_fin_dt,
            localidad=localidad
        )

        precio = 100
        fecha = timezone.now()
        Boleto.objects.create(evento=evento, precio=precio, fecha=fecha)

        # Enviar respuesta JSON con los datos del evento creado
        return JsonResponse({
            'id': evento.id,
            'name': evento.name,
            'fecha_inicio': evento.fecha_inicio,
            'fecha_fin': evento.fecha_fin,
            'localidad_name': evento.localidad.name
        })

    localidades = Localidad.objects.all()
    eventos = Evento.objects.order_by('-id')[:5]  # Últimos 5 eventos creados
    return render(request, 'agregar_evento.html', {'localidades': localidades, 'eventos': eventos})


# Vista para eliminar un evento
@require_http_methods(["DELETE"])
def eliminar_evento(request, evento_id):
    try:
        evento = Evento.objects.get(id=evento_id)
        evento.delete()
        return JsonResponse({'success': True})
    except Evento.DoesNotExist:
        return JsonResponse({'error': 'Evento no encontrado'}, status=404)




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


def agregar_boleto(request):
    if request.method == 'POST':
        evento_id = request.POST.get('evento')
        precio = float(request.POST.get('precio'))

        if not evento_id or not precio:
            return JsonResponse({'error': 'El evento y el precio son obligatorios'}, status=400)

        evento = Evento.objects.get(id=evento_id)
        fecha = timezone.now()

        boleto = Boleto.objects.create(
            precio=precio,
            evento=evento,
            fecha=fecha
        )

        return JsonResponse({
            'id': boleto.id,
            'evento_name': boleto.evento.name,
            'precio': boleto.precio,
            'fecha': boleto.fecha.strftime('%Y-%m-%d %H:%M'),
        })

    eventos = Evento.objects.all()
    boletos = Boleto.objects.order_by('-fecha')[:5]  # Últimos 5 boletos creados
    return render(request, 'agregar_boleto.html', {'eventos': eventos, 'boletos': boletos})

@require_http_methods(["POST"])
def eliminar_boleto(request, boleto_id):
    try:
        boleto = Boleto.objects.get(id=boleto_id)
        boleto.delete()
        return JsonResponse({'success': True})
    except Boleto.DoesNotExist:
        return JsonResponse({'error': 'Boleto no encontrado'}, status=404)
