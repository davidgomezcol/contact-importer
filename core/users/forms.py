from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterUserForm(UserCreationForm):
    """Form to register a new user"""
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
