from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm, Form

from markdown import markdown

from shop.models import Order
from docs.models import Document
from factory.models import Task, User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
