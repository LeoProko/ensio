from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from factory.html_factories.base import BaseHtmlFactory
from factory.models import Customer
from factory.forms import CustomerForm
from factory.decorators import allowed_users


@login_required(login_url='login')
@allowed_users(allowed_users_list=['cashier'])
def customers(request):
    customers = Customer.objects.all()
    customers_count = customers.count()
    template = Template(BaseHtmlFactory.create.back_office(
        'Customers', 'back_office', 'customers', '', ''
    ))
    context = Context({
        'request' : request,
        'customers' : customers,
        'customers_count' : customers_count,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@login_required(login_url='login')
@allowed_users(allowed_users_list=['cashier'])
def new_customer(request):
    template = Template(BaseHtmlFactory.create.back_office(
        'New customer', 'back_office', 'new_customer', '', ''
    ))
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
@allowed_users(allowed_users_list=['cashier'])
def customer_profile(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    orders = customer.customerorder_set.all()
    orders_count = orders.count()
    template = Template(BaseHtmlFactory.create.back_office(
        customer.first_name, 'back_office', 'customer_profile', '', ''
    ))

    context = Context({
        'request' : request,
        'customer' : customer,
        'orders' : orders,
        'orders_count' : orders_count,
    })
    return HttpResponse(template.render(context))