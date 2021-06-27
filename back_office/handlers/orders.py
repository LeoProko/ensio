from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import redirect
from django.forms import inlineformset_factory, modelformset_factory
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from frontend_server.html_factories.base import BaseHtmlFactory
from frontend_server.models import Customer, Order
from frontend_server.forms import OrderForm
from frontend_server.filters import OrderFilter
from frontend_server.decorators import allowed_users


@login_required(login_url='login')
@allowed_users(allowed_users_list=['cashier'])
def orders(request):
    template = Template(BaseHtmlFactory.create.back_office('Orders', 'back_office/templates/', 'orders', '', ''))
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
@allowed_users(allowed_users_list=['cashier'])
def new_order(request):
    # OrderFormSet = inlineformset_factory(Customer, Order, fields=('customer', 'item', 'status'), extra=5)
    template = Template(BaseHtmlFactory.create.back_office('New order', 'back_office/templates/', 'new_order', '', ''))
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
@allowed_users(allowed_users_list=[])
def new_order_by_customer(request, customer_id):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('item', 'status'), extra=5)
    customer = Customer.objects.get(id=customer_id)
    template = Template(BaseHtmlFactory.create.back_office('New order', 'back_office/templates/', 'new_order', '', ''))
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
@allowed_users(allowed_users_list=[])
def change_order(request, order_id):
    template = Template(BaseHtmlFactory.create.back_office('Change order', 'back_office/templates/', 'new_order', '', ''))
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
@allowed_users(allowed_users_list=[])
def delete_order(request, order_id):
    template = Template(BaseHtmlFactory.create.back_office('Delete order', 'back_office/templates/', 'delete_order', '', ''))
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('/customers/')

    context = Context({
        'request' : request,
        'order' : order,
    })
    return HttpResponse(template.render(context))