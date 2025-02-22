from django import forms
from .models import User, UserAddress

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'age', 'rfc', 'photo']

class UserAddressForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        fields = ['street', 'zip_code', 'city', 'country']
