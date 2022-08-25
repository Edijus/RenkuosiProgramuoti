from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Order, OrderDetail


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'vehicle', 'image']


class CreateOrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = ['service', 'order', 'quantity']


class EditUserAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'image']
