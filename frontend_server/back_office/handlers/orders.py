from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import redirect
from django.forms import inlineformset_factory, modelformset_factory
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from factory.html_factories.base import BaseHtmlFactory
from factory.models import Customer, CustomerOrder, Order
from factory.forms import OrderForm
from factory.filters import OrderFilter
from factory.decorators import allowed_users


@login_required(login_url='login')
@allowed_users(allowed_users_list=['cashier'])
def orders(request):
    template = Template(BaseHtmlFactory.create.back_office(
        'Orders', 'back_office', 'orders', '', ''
    ))
    orders = Order.objects.all()
    order_counter = orders.count()
    order_counters = []
    for status in [
            'Получен',
            'В работе',
            'Готовится к доставке',
            'В пути',
            'Доставлен',
    ]:
        order_counters.append([
            status,
            Order.objects.filter(status=status).count()
        ])
    filter = OrderFilter(request.GET, queryset=orders)
    orders = filter.qs
    context = Context({
        'request' : request,
        'orders': reversed(orders),
        'order_counter': order_counter,
        'order_counters': order_counters,
        'filter' : filter,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@login_required(login_url='login')
@allowed_users(allowed_users_list=['cashier'])
def new_order(request):
    # CustomerOrderFormSet = inlineformset_factory(Customer, CustomerOrder, fields=('customer', 'item', 'status'), extra=5)
    template = Template(BaseHtmlFactory.create.back_office(
        'New order', 'back_office', 'new_order', '', ''
    ))
    # order_form_set = CustomerOrderFormSet(queryset=CustomerOrder.objects.none())
    order_form = OrderForm()

    if request.method == 'POST':
        order_form= OrderForm(request.POST)
        if order_form.is_valid():
            order_form.save()
            print('New order has been created', request.POST)
            return redirect('/back_office/orders')

    context = Context({
        'request' : request,
        'forms' : [order_form],
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@login_required(login_url='login')
@allowed_users(allowed_users_list=[])
def new_order_by_customer(request, customer_id):
    CustomerOrderFormSet = inlineformset_factory(Customer, CustomerOrder, fields=('item', 'status'), extra=5)
    customer = Customer.objects.get(id=customer_id)
    template = Template(BaseHtmlFactory.create.back_office(
        'New order', 'back_office', 'new_order', '', ''
    ))
    # order_form = CustomerOrderForm(initial={'customer' : customer})
    order_form_set = CustomerOrderFormSet(queryset=CustomerOrder.objects.none(), instance=customer)

    if request.method == 'POST':
        # form = CustomerOrderForm(request.POST)
        order_form_set = CustomerOrderFormSet(request.POST, instance=customer)
        if order_form_set.is_valid():
            order_form_set.save()
            print('New order has been created', request.POST)
            return redirect('/back_office/customers/' + str(customer.id))

    context = Context({
        'request' : request,
        'customer' : customer,
        'forms' : order_form_set,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@login_required(login_url='login')
@allowed_users(allowed_users_list=[])
def change_order(request, order_id):
    template = Template(BaseHtmlFactory.create.back_office(
        'Change order', 'back_office', 'new_order', '', ''
    ))
    order = Order.objects.get(id=order_id)
    order_form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            print('CustomerOrder', order_id, 'has been changed', request.POST)
            return redirect('/back_office/orders')

    context = Context({
        'request' : request,
        'forms' : [order_form],
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@login_required(login_url='login')
@allowed_users(allowed_users_list=[])
def delete_order(request, order_id):
    template = Template(BaseHtmlFactory.create.back_office(
        'Delete order', 'back_office', 'delete_order', '', ''
    ))
    order = CustomerOrder.objects.get(id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('/back_office/customers')

    context = Context({
        'request' : request,
        'order' : order,
    })
    return HttpResponse(template.render(context))
