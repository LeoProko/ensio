from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm, Form

from markdown import markdown

from factory.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='username', widget=forms.TextInput(
        attrs={
            'Placeholder' : 'Username',
        }
    ))
    email = forms.EmailField(label='email', widget=forms.TextInput(
        attrs={
            'Placeholder' : 'E-mail',
        }
    ))
    phone_number = forms.CharField(label='phone_number', widget=forms.TextInput(
        attrs={
            'Placeholder' : 'Phone number',
        }
    ))
    password1 = forms.CharField(label='password1', widget=forms.PasswordInput(
        attrs={
            'Placeholder' : 'Password',
        }
    ))
    password2 = forms.CharField(label='password2', widget=forms.PasswordInput(
        attrs={
            'Placeholder' : 'Repeat password',
        }
    ))

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']

class LoginForm(Form):
    email = forms.EmailField(label='email', widget=forms.TextInput(
        attrs={
            'Placeholder' : 'E-mail',
        }
    ))
    password = forms.CharField(label='password', widget=forms.PasswordInput(
        attrs={
            'Placeholder' : 'Password',
        }
    ))
