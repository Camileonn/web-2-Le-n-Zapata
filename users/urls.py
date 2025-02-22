from django.urls import path
from .views import usersIndex, createuser, userdetail, edit_user, mainPage , createuser# Agrupé todas las vistas



urlpatterns = [
    # Ruta para la página principal
    path('', mainPage, name='main_page'),  # Página principal que redirige a 'index.html'

    # Rutas para la gestión de usuarios
    path('users/', usersIndex, name='users_index'),  # Lista de usuarios
    path('create/', createuser, name="create_user"),  # Ruta para crear un usuario
    path('detail/<int:id>/', userdetail, name="user_detail"),  # Detalles de un usuario específico
    path('edit/<int:id>/', edit_user, name="edit_user"),
]
