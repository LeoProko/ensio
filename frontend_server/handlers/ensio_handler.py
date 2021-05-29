from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from frontend_server.html_factories.custom import CustomHtmlFactory
from frontend_server.models import Password, Employee, Item, Customer, Order
from frontend_server.forms import OrderForm

def index(request):
    template = Template(CustomHtmlFactory.create('Ensio', 'main', 'main', ''))
    context = Context({})
    return HttpResponse(template.render(context))

def customers(request):
    customers = Customer.objects.all()
    customers_count = customers.count()
    template = Template(CustomHtmlFactory.create('Customers', 'customers', '', ''))
    context = Context({
        'customers' : customers,
        'customers_count' : customers_count,
    })
    return HttpResponse(template.render(context))

def customer_profile(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    orders = customer.order_set.all()
    orders_count = orders.count()
    template = Template(CustomHtmlFactory.create(customer.first_name, 'customer_profile', '', ''))
    context = Context({
        'customer' : customer,
        'orders' : orders,
        'orders_count' : orders_count,
    })
    return HttpResponse(template.render(context))

def orders(request):
    template = Template(CustomHtmlFactory.create('Orders', 'orders', '', ''))
    orders = Order.objects.all()
    orders_count = orders.count()
    context = Context({
        'orders': orders,
        'orders_count': orders_count,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
def new_order(request):
    template = Template(CustomHtmlFactory.create('New order', 'new_order', '', ''))
    order_form = OrderForm()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            print('New order has been created', request.POST)
            return redirect('orders')

    context = Context({
        'form' : order_form,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
def change_order(request, order_id):
    template = Template(CustomHtmlFactory.create('New order', 'new_order', '', ''))
    order = Order.objects.get(id=order_id)
    order_form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            print('New order has been created', request.POST)
            return redirect('orders')

    context = Context({
        'form' : order_form,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
def delete_order(request, order_id):
    template = Template(CustomHtmlFactory.create('Delete order', 'delete_order', '', ''))
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('orders')

    context = Context({
        'order' : order,
    })
    return HttpResponse(template.render(context))

def items(request):
    template = Template(CustomHtmlFactory.create('Items', 'items', '', ''))
    context = Context({})
    return HttpResponse(template.render(context))

def show_all_employees(request):
    employees = Employee.objects.all()
    status_count = {
        'works' : employees.filter(status='Works').count(),
        'on_holiday' : employees.filter(status='On holiday').count(),
        'dismissed' : employees.filter(status='Dismissed').count(),
    }
    employees_count = employees.count()
    template = Template(CustomHtmlFactory.create('Employees', 'employees', '', ''))
    context = Context({
        'employees': employees,
        'employees_count': employees_count,
        'status_count': status_count,
    })
    return HttpResponse(template.render(context))

def password(request):
    passwords = Password.objects.all()
    passwords_count = passwords.count()
    template = Template(CustomHtmlFactory.create('Passwords', 'passwords', '', ''))
    context = Context({
        'passwords': passwords,
        'passwords_count': passwords_count,
    })
    return HttpResponse(template.render(context))
