from django.shortcuts import render, redirect
from .models import User
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json
from .models import User, UserAddress
from .forms import UserForm, UserAddressForm
from django.http import HttpResponse





def usersIndex(request):
    users = User.objects.all()  
    return render(request, 'users/Users.html', {'users': users})

def mainPage(request):
    return render(request, 'users/index.html')


def createuserview(request):
    return render(request, "users/create.html")

def createuser(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        rfc = request.POST.get('rfc')
        photo = request.POST.get('photo')

        # Crear el usuario en la base de datos
        user = User.objects.create(name=name, email=email, age=age, rfc=rfc, photo=photo)

        return redirect('user_details', user_id=user.id)  # Redirige a la página de detalles del usuario.
    
    return render(request, 'create.html')



"mejor usar el error 404 para que os mande el error "
def userdetail(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, "users/detail.html", {"user": user})





def edit_user(request, id):  # Cambié 'user_id' a 'id'
    user = get_object_or_404(User, id=id)  # Obtener el usuario por ID
    addresses = UserAddress.objects.filter(user=user)  # Obtener las direcciones asociadas al usuario

    if request.method == 'POST':
        # Formulario para editar el usuario
        user_form = UserForm(request.POST, instance=user)
        # Formulario para editar las direcciones
        address_forms = []
        for address in addresses:
            form = UserAddressForm(request.POST, instance=address)
            address_forms.append(form)

        if user_form.is_valid() and all(form.is_valid() for form in address_forms):
            user_form.save()  # Guardar la información actualizada del usuario
            for form in address_forms:
                form.save()  # Guardar las direcciones actualizadas
            return redirect('users_index') # Redirige a la lista de usuarios después de la actualización
    else:
        # Mostrar los formularios con los datos actuales
        user_form = UserForm(instance=user)
        address_forms = [UserAddressForm(instance=address) for address in addresses]

    return render(request, 'users/edit_user.html', {
        'user_form': user_form, 
        'user': user, 
        'addresses': addresses,
        'address_forms': address_forms
    })
