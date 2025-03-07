from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('eventos/', views.eventos, name='eventos'),
    path('boletos/', views.boletos, name='boletos'),
    path('agregar_evento/', views.agregar_evento, name='agregar_evento'),
    path('eliminar_evento/<int:evento_id>/', views.eliminar_evento, name='eliminar_evento'),
    path('boletos/<int:evento_id>/', views.ver_boletos, name='boletos'),
    path('agregar_boleto/', views.agregar_boleto, name='agregar_boleto'),
    path('eliminar_boleto/<int:boleto_id>/', views.eliminar_boleto, name='eliminar_boleto'),


    

]
