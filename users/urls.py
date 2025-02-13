from django.urls import path
from .views import usersIndex

urlpatterns = [
    path('', usersIndex, name='users_index'),
]