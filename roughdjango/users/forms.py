from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginPageForm(forms.Form):
    username = forms.CharField(label = 'User Name', max_length = 35)
    password = forms.CharField(label = 'Password', max_length = 35, widget = forms.PasswordInput)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']