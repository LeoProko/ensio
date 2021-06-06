from django.contrib.auth.forms import UserCreationForm
from  django.contrib.auth.models import User
from  django.forms import ModelForm

from markdown import markdown

from .models import Customer, Order, Employee, Document

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

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
