from django.shortcuts import render

from django.shortcuts import render
from .models import User

def usersIndex(request):
    users = User.objects.all()  # Sin direcciones
    return render(request, 'users/index.html', {'users': users})

