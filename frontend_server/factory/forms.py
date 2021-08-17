from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm, Form

from markdown import markdown

from .models import Order, Document, Task, User

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class FastOrderForm(Form):
    CONNECTION = (
        ('Phone', 'Телефон'),
        ('Telegram', 'Телеграм'),
        ('Whats App', 'Вотс ап'),
    )
    size = forms.ChoiceField(choices=[])
    customer_name = forms.CharField(max_length=50, label='Имя', widget=forms.TextInput(
        attrs={
            'Placeholder' : 'Имя',
        }
    ))
    connection_type = forms.ChoiceField(choices=CONNECTION, widget=forms.RadioSelect)
    phone_number = forms.CharField(max_length=50, label='Номер телефона', widget=forms.TextInput(
        attrs={
            'Placeholder' : 'Номер телефона',
        }
    ))

class RegisterForm(UserCreationForm):
    phone_number = forms.CharField(max_length=12)
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']

class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
        exclude = ['html_data', 'owner', 'preview']

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

class TrackOrderForm(forms.Form):
    order_id = forms.CharField(max_length=12, widget=forms.TextInput(
        attrs={
            'Placeholder' : 'Номер заказа'
        }
    ))
