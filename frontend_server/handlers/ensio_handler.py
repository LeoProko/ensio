from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import redirect
from django.forms import inlineformset_factory, modelformset_factory
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from markdown import markdown

from frontend_server.html_factories.base import BaseHtmlFactory
from frontend_server.models import Password, Employee, Item, Customer, Order, Document, Task
from frontend_server.forms import CustomerForm, OrderForm, EmployeeForm, RegisterForm, DocumentForm, TaskForm
from frontend_server.filters import OrderFilter, ItemFilter
from frontend_server.decorators import unauthenticated_user, allowed_users


@login_required(login_url='login')
@allowed_users(allowed_users=[])
def index(request):
    template = Template(BaseHtmlFactory.create('Ensio', 'main', '', ''))
    context = Context({
        'request' : request,
    })
    return HttpResponse(template.render(context))

@login_required(login_url='login')
@allowed_users(allowed_users=['cashier'])
def customers(request):
    customers = Customer.objects.all()
    customers_count = customers.count()
    template = Template(BaseHtmlFactory.create('Customers', 'customers', '', ''))
    context = Context({
        'request' : request,
        'customers' : customers,
        'customers_count' : customers_count,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@login_required(login_url='login')
@allowed_users(allowed_users=['cashier'])
def new_customer(request):
    template = Template(BaseHtmlFactory.create('New customer', 'new_customer', '', ''))
    customer_form = CustomerForm()

    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()
            print('New customer has been created', request.POST)
            return redirect('/customers/')

    context = Context({
        'request' : request,
        'form' : customer_form,
    })
    return HttpResponse(template.render(context))

@login_required(login_url='login')
@allowed_users(allowed_users=['cashier'])
def customer_profile(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    orders = customer.order_set.all()
    orders_count = orders.count()
    template = Template(BaseHtmlFactory.create(customer.first_name, 'customer_profile', '', ''))

    context = Context({
        'request' : request,
        'customer' : customer,
        'orders' : orders,
        'orders_count' : orders_count,
    })
    return HttpResponse(template.render(context))

@login_required(login_url='login')
@allowed_users(allowed_users=['cashier'])
def orders(request):
    template = Template(BaseHtmlFactory.create('Orders', 'orders', '', ''))
    orders = Order.objects.all()
    orders_count = [orders.count()]
    for status in ['Received', 'In work', 'Ready to deliver', 'On the way', 'Delivered']:
        orders_count.append(Order.objects.filter(status=status).count())
    filter = OrderFilter(request.GET, queryset=orders)
    orders = filter.qs
    context = Context({
        'request' : request,
        'orders': orders,
        'orders_count': orders_count,
        'filter' : filter,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@login_required(login_url='login')
@allowed_users(allowed_users=['cashier'])
def new_order(request):
    # OrderFormSet = inlineformset_factory(Customer, Order, fields=('customer', 'item', 'status'), extra=5)
    template = Template(BaseHtmlFactory.create('New order', 'new_order', '', ''))
    # order_form_set = OrderFormSet(queryset=Order.objects.none())
    order_form = OrderForm()

    if request.method == 'POST':
        order_form= OrderForm(request.POST)
        if order_form.is_valid():
            order_form.save()
            print('New order has been created', request.POST)
            return redirect('/orders/')

    context = Context({
        'request' : request,
        'forms' : [order_form],
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@login_required(login_url='login')
@allowed_users(allowed_users=[])
def new_order_by_customer(request, customer_id):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('item', 'status'), extra=5)
    customer = Customer.objects.get(id=customer_id)
    template = Template(BaseHtmlFactory.create('New order', 'new_order', '', ''))
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
        'request' : request,
        'customer' : customer,
        'forms' : order_form_set,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@login_required(login_url='login')
@allowed_users(allowed_users=[])
def change_order(request, order_id):
    template = Template(BaseHtmlFactory.create('Change order', 'new_order', '', ''))
    order = Order.objects.get(id=order_id)
    order_form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            print('Order', order_id, 'has been changed', request.POST)
            return redirect('/orders/')

    context = Context({
        'request' : request,
        'forms' : [order_form],
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@login_required(login_url='login')
@allowed_users(allowed_users=[])
def delete_order(request, order_id):
    template = Template(BaseHtmlFactory.create('Delete order', 'delete_order', '', ''))
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('/customers/')

    context = Context({
        'request' : request,
        'order' : order,
    })
    return HttpResponse(template.render(context))

@login_required(login_url='login')
@allowed_users(allowed_users=[])
def show_all_employees(request):
    employees = Employee.objects.all()
    status_count = {
        'works' : employees.filter(status='Works').count(),
        'on_holiday' : employees.filter(status='On holiday').count(),
        'dismissed' : employees.filter(status='Dismissed').count(),
    }
    employees_count = employees.count()
    template = Template(BaseHtmlFactory.create('Employees', 'employees', '', ''))
    context = Context({
        'request' : request,
        'employees': employees,
        'employees_count': employees_count,
        'status_count': status_count,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@login_required(login_url='login')
@allowed_users(allowed_users=[])
def new_employee(request):
    template = Template(BaseHtmlFactory.create('New employee', 'new_employee', '', ''))
    employee_form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            print('New employee has been created', request.POST)
            return redirect('/employees/')

    context = Context({
        'request' : request,
        'form' : employee_form,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@login_required(login_url='login')
@allowed_users(allowed_users=[])
def change_employee(request, employee_id):
    template = Template(BaseHtmlFactory.create('Change employee', 'new_employee', '', ''))
    employee = Employee.objects.get(id=employee_id)
    employee_form = EmployeeForm(instance=employee)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            print('Employee', employee_id, 'has been changed', request.POST)
            return redirect('/employees/')

    context = Context({
        'request' : request,
        'form' : employee_form,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@login_required(login_url='login')
@allowed_users(allowed_users=[])
def delete_employee(request, employee_id):
    template = Template(BaseHtmlFactory.create('Delete employee', 'delete_employee', '', ''))
    employee = Employee.objects.get(id=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('/employees/')

    context = Context({
        'request' : request,
        'employee' : employee,
    })
    return HttpResponse(template.render(context))

@login_required(login_url='login')
@allowed_users(allowed_users=[])
def password(request):
    passwords = Password.objects.all()
    passwords_count = passwords.count()
    template = Template(BaseHtmlFactory.create('Passwords', 'passwords', '', ''))
    context = Context({
        'request' : request,
        'passwords' : passwords,
        'passwords_count' : passwords_count,
    })
    return HttpResponse(template.render(context))

@login_required(login_url='login')
@allowed_users(allowed_users=[])
def get_stock(request):
    template = Template(BaseHtmlFactory.create('Stock', 'stock', '', ''))

    items = Item.objects.all()
    items_count = items.count()
    filter = ItemFilter(request.GET, queryset=items)
    items = filter.qs

    context = Context({
        'request' : request,
        'items' : items,
        'filter' : filter,
        'items_count' : items_count,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@unauthenticated_user
def user_login(request):
    template = Template(BaseHtmlFactory.create('Login', 'login', '', ''))
    context = Context({
        'request' : request,
    })
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        messages.info(request, 'Username or password in incorrect')
    return HttpResponse(template.render(context))

@csrf_exempt
@unauthenticated_user
def user_register(request):
    template = Template(BaseHtmlFactory.create('Register', 'register', '', ''))
    form  = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            group = Group.objects.get(name='guest')
            user.groups.add(group)
            messages.success(request, username + ' has been registered')
            return redirect('index')

    context = Context({
        'request' : request,
        'form' : form
    })
    return HttpResponse(template.render(context))

def user_logout(request):
    logout(request)
    return redirect('login')

def no_permissions(request):
    template = Template(BaseHtmlFactory.create('No permissions', 'no_permissions', '', ''))
    context = Context({
        'request' : request,
    })
    return HttpResponse(template.render(context))

@login_required(login_url='login')
@allowed_users(allowed_users=[])
def get_documents(request):
    template = Template(BaseHtmlFactory.create('Documents', 'documents', '', ''))
    documents = Document.objects.all()
    documents_count = documents.count()
    context = Context({
        'documents' : documents,
        'documents_count' : documents_count,
        'request' : request,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@login_required(login_url='login')
@allowed_users(allowed_users=['cashier'])
def new_document(request):
    template = Template(BaseHtmlFactory.create('New document', 'new_document', '', ''))
    document_form = DocumentForm(initial={'owner':request.user})

    if request.method == 'POST':
        document_form = DocumentForm(request.POST)
        if document_form.is_valid():
            form = document_form.save(commit=False)
            form.html_data = markdown(form.markdown_data)
            form.save()
            print('New document has been created', request.POST)
            return redirect('/documents/')

    context = Context({
        'request' : request,
        'form' : document_form,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@login_required(login_url='login')
@allowed_users(allowed_users=[])
def edit_document(request, document_id):
    template = Template(BaseHtmlFactory.create('Document', 'new_document', '', ''))
    document = Document.objects.get(id=document_id)
    document_form = DocumentForm(instance=document)
    if request.method == 'POST':
        document_form = DocumentForm(request.POST, instance=document)
        if document_form.is_valid():
            form = document_form.save(commit=False)
            form.html_data = markdown(form.markdown_data)
            form.save()
            print('Document', document_id, 'has been changed', request.POST)
            return redirect('/edit_document/' + document_id)

    context = Context({
        'request' : request,
        'document' : document,
        'form' : document_form,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@login_required(login_url='login')
@allowed_users(allowed_users=[])
def view_document(request, document_id):
    template = Template(BaseHtmlFactory.create('Document', 'document', '', ''))
    document = Document.objects.get(id=document_id)
    context = Context({
        'request' : request,
        'document' : document,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@login_required(login_url='login')
@allowed_users(allowed_users=[])
def delete_document(request, document_id):
    template = Template(BaseHtmlFactory.create('Remove document', 'delete_document', '', ''))
    document = Document.objects.get(id=document_id)
    if request.method == 'POST':
        document.delete()
        return redirect('/documents/')

    context = Context({
        'request' : request,
        'document' : document,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@login_required(login_url='login')
@allowed_users(allowed_users=[])
def get_tasks(request):
    template = Template(BaseHtmlFactory.create('Tasks', 'tasks', '', ''))
    tasks = Task.objects.all()
    tasks_count = tasks.count()
    TaskFormSet = modelformset_factory(Task, form=TaskForm)
    task_form_set = TaskFormSet(queryset=tasks)
    if request.method == 'POST':
        for index, form in enumerate(task_form_set):
            print("index:::::::::", index, request.POST)
            form = TaskForm(request.POST, initial={
                'done' : request.POST.get('form-' + str(index) + '-done'),
                'task' : request.POST.get('form-' + str(index) + '-task'),
                'deadline' : request.POST.get('form-' + str(index) + '-deadline'),
                'chief' : request.POST.get('form-' + str(index) + '-chief'),
                'executors' : request.POST.get('form-' + str(index) + '-executors'),
            })
            form.save()
            if form.is_valid():
                form.save()

        return redirect('/tasks/')
        # for key, value in request.POST.items():
            # print("TASK REQUEST", key, value)
        # print("TASK RECEIVED", request.POST.get('form-1-done'))
        # task_form = TaskForm(request.POST)
        # if task_form.is_valid():
            # task_form.save()
            # return redirect('/tasks/')

    context = Context({
        'request' : request,
        'tasks' : tasks,
        'tasks_count' : tasks_count,
        'task_set' : task_form_set,
    })
    return HttpResponse(template.render(context))
