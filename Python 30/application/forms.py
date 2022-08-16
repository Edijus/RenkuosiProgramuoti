from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignUpForm(UserCreationForm):
    email_address = forms.EmailField()
    image = forms.ImageField()

    class Meta:
        model = User
        fields = ['username', 'email_address', 'password1', 'password2', 'image']