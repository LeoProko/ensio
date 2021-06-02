from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import redirect
from django.forms import inlineformset_factory
from django.views.decorators.csrf import csrf_exempt

from frontend_server.html_factories.custom import CustomHtmlFactory
from frontend_server.models import Password, Employee, Item, Customer, Order
from frontend_server.forms import CustomerForm, OrderForm, EmployeeForm
from frontend_server.filters import OrderFilter, ItemFilter

def index(request):
    template = Template(CustomHtmlFactory.create('Ensio', 'main', '', ''))
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

@csrf_exempt
def new_customer(request):
    template = Template(CustomHtmlFactory.create('New customer', 'new_customer', '', ''))
    customer_form = CustomerForm()

    if request.method == 'POST':
        customer_form= CustomerForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()
            print('New customer has been created', request.POST)
            return redirect('/customers/')

    context = Context({
        'form' : customer_form,
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
    orders_count = [orders.count()]
    for status in ['Received', 'In work', 'Ready to deliver', 'On the way', 'Delivered']:
        orders_count.append(Order.objects.filter(status=status).count())
    filter = OrderFilter(request.GET, queryset=orders)
    orders = filter.qs
    context = Context({
        'orders': orders,
        'orders_count': orders_count,
        'filter' : filter,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
def new_order(request):
    # OrderFormSet = inlineformset_factory(Customer, Order, fields=('customer', 'item', 'status'), extra=5)
    template = Template(CustomHtmlFactory.create('New order', 'new_order', '', ''))
    # order_form_set = OrderFormSet(queryset=Order.objects.none())
    order_form = OrderForm()

    if request.method == 'POST':
        order_form= OrderForm(request.POST)
        if order_form.is_valid():
            order_form.save()
            print('New order has been created', request.POST)
            return redirect('/orders/')

    context = Context({
        'forms' : [order_form],
    })
    return HttpResponse(template.render(context))

@csrf_exempt
def new_order_by_customer(request, customer_id):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('item', 'status'), extra=5)
    customer = Customer.objects.get(id=customer_id)
    template = Template(CustomHtmlFactory.create('New order', 'new_order', '', ''))
    # order_form = OrderForm(initial={'customer' : customer})
    order_form_set = OrderFormSet(queryset=Order.objects.none(), instance=customer)

    if request.method == 'POST':
        # form = OrderForm(request.POST)
        order_form_set = OrderFormSet(request.POST, instance=customer)
        if order_form_set.is_valid():
            order_form_set.save()
            print('New order has been created', request.POST)
            return redirect('/customers/' + str(customer.id))

    context = Context({
        'customer' : customer,
        'forms' : order_form_set,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
def change_order(request, order_id):
    template = Template(CustomHtmlFactory.create('Change order', 'new_order', '', ''))
    order = Order.objects.get(id=order_id)
    order_form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            print('Order', order_id, 'has been changed', request.POST)
            return redirect('/customers/')

    context = Context({
        'forms' : [order_form],
    })
    return HttpResponse(template.render(context))

@csrf_exempt
def delete_order(request, order_id):
    template = Template(CustomHtmlFactory.create('Delete order', 'delete_order', '', ''))
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('/customers/')

    context = Context({
        'order' : order,
    })
    return HttpResponse(template.render(context))

def items(request):
    template = Template(CustomHtmlFactory.create('Items', 'items', '', ''))
    context = Context({})
    return HttpResponse(template.render(context))

@csrf_exempt
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

@csrf_exempt
def new_employee(request):
    template = Template(CustomHtmlFactory.create('New employee', 'new_employee', '', ''))
    employee_form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            print('New employee has been created', request.POST)
            return redirect('/employees/')

    context = Context({
        'form' : employee_form,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
def change_employee(request, employee_id):
    template = Template(CustomHtmlFactory.create('Change employee', 'new_employee', '', ''))
    employee = Employee.objects.get(id=employee_id)
    employee_form = EmployeeForm(instance=employee)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            print('Employee', employee_id, 'has been changed', request.POST)
            return redirect('/employees/')

    context = Context({
        'form' : employee_form,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
def delete_employee(request, employee_id):
    template = Template(CustomHtmlFactory.create('Delete employee', 'delete_employee', '', ''))
    employee = Employee.objects.get(id=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('/employees/')

    context = Context({
        'employee' : employee,
    })
    return HttpResponse(template.render(context))

def password(request):
    passwords = Password.objects.all()
    passwords_count = passwords.count()
    template = Template(CustomHtmlFactory.create('Passwords', 'passwords', '', ''))
    context = Context({
        'passwords' : passwords,
        'passwords_count' : passwords_count,
    })
    return HttpResponse(template.render(context))

def get_stock(request):
    template = Template(CustomHtmlFactory.create('Stock', 'stock', '', ''))

    items = Item.objects.all()
    items_count = items.count()
    filter = ItemFilter(request.GET, queryset=items)
    items = filter.qs

    context = Context({
        'items' : items,
        'filter' : filter,
        'items_count' : items_count,
    })
    return HttpResponse(template.render(context))

