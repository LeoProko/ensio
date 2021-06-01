from  django.forms import ModelForm
from .models import Order, Employee

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
