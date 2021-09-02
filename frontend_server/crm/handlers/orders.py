from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import redirect
from django.forms import inlineformset_factory, modelformset_factory
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django_hosts.resolvers import reverse

from factory.html_factories.base import BaseHtmlFactory
from crm.models import Order
from crm.forms import OrderForm
from crm.filters import OrderFilter
from factory.decorators import allowed_users

@login_required(login_url=reverse('login', host='base'))
@allowed_users(allowed_users_list=['cashier'])
def orders(request):
    template = Template(BaseHtmlFactory.create.new_create(
        'crm', 'Orders', 'orders'
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
@login_required(login_url=reverse('login', host='base'))
@allowed_users(allowed_users_list=['cashier'])
def change_order(request, order_id):
    template = Template(BaseHtmlFactory.create.new_create(
        'crm', 'Change order', 'new_order'
    ))
    order = Order.objects.get(id=order_id)
    order_form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            print('CustomerOrder', order_id, 'has been changed', request.POST)
            return redirect('/orders')

    context = Context({
        'request' : request,
        'form' : order_form,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@login_required(login_url=reverse('login', host='base'))
def remove_order(request, order_id):
    template = Template(BaseHtmlFactory.create.new_create(
        'crm', 'Remove order', 'remove_order'
    ))
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('/orders')

    context = Context({
        'request' : request,
        'order' : order,
    })
    return HttpResponse(template.render(context))
