from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    bio = forms.CharField(max_length=300)

    class Meta:
        model = User
        fields = ['username', 'email', 'bio', 'password1', 'password2']