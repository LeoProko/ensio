from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm, Form

from markdown import markdown

from .models import Customer, CustomerOrder, Order, Employee, Document, Task

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class CustomerOrderForm(ModelForm):
    class Meta:
        model = CustomerOrder
        fields = '__all__'

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class FastOrderForm(Form):
    CONNECTION = (
        ('Phone', 'Телефон'),
        ('Telegram', 'Телеграм'),
        ('Whats App', 'Вотс ап'),
        ('Instagram', 'Инстаграм'),
    )

    SIZE = (
        ('15', '15'),
        ('15.5', '15.5'),
        ('16', '16'),
        ('16.5', '16.5'),
        ('17', '17'),
        ('17.5', '17.5'),
        ('18', '18'),
        ('18.5', '18.5'),
        ('19', '19'),
        ('19.5', '19.5'),
        ('20', '20'),
        ('20.5', '20.5'),
        ('21', '21'),
    )

    customer_name = forms.CharField(max_length=50, label='Имя', widget=forms.TextInput(
        attrs={
            'Placeholder' : 'Имя',
        }))
    connection_type = forms.ChoiceField(choices=CONNECTION, widget=forms.RadioSelect)
    contacts = forms.CharField(max_length=50, label='Номер телефона/Ник', widget=forms.TextInput(
        attrs={
            'Placeholder' : 'Номре телефона/Ник',
        }))

    size = forms.ChoiceField(choices=SIZE)


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
        exclude = ['html_data']

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
