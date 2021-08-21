from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm, Form

from markdown import markdown

from .models import Order

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

class TrackOrderForm(forms.Form):
    order_id = forms.CharField(max_length=12, widget=forms.TextInput(
        attrs={
            'Placeholder' : 'Номер заказа'
        }
    ))
