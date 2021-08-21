from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import redirect
from django.forms import inlineformset_factory, modelformset_factory
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from factory.html_factories.base import BaseHtmlFactory
from shop.models import Order
from shop.forms import OrderForm
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
        'form' : order_form,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@login_required(login_url='login')
@allowed_users(allowed_users_list=[])
def delete_order(request, order_id):
    template = Template(BaseHtmlFactory.create.back_office(
        'Delete order', 'back_office', 'delete_order', '', ''
    ))
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('/back_office/orders')

    context = Context({
        'request' : request,
        'order' : order,
    })
    return HttpResponse(template.render(context))
