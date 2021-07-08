from django.http import HttpResponse, HttpResponseNotFound
from django.template  import Template, Context
from django.shortcuts import redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from frontend_server.html_factories.base import BaseHtmlFactory
from frontend_server.forms import FastOrderForm
from frontend_server.models import Order, Item


@csrf_exempt
def index(request, landing_id):
    # landing_id HAVE TO be the same as name of Item
    try:
        template = Template(BaseHtmlFactory.create.empty(
            'Landing', 'landing/templates/', landing_id, landing_id, ''))
    except:
        return HttpResponseNotFound('Ooops... 404 error')

    order_form = FastOrderForm()

    if request.method == 'POST':
        order_form = FastOrderForm(request.POST)
        if order_form.is_valid():
            customer_name = order_form.cleaned_data['customer_name']
            connection_type = order_form.cleaned_data['connection_type']
            contacts = order_form.cleaned_data['contacts']
            size = order_form.cleaned_data['size']
            item = Item.objects.get(name=landing_id)

            new_order = Order.objects.create(item=item,
                              customer_name=customer_name,
                              connection_type=connection_type,
                              contacts=contacts,
                              size=size,
                              date_created=timezone.now())
            new_order.save()

            print('New Order has been created', request.POST)
            return redirect('/track_order/' + str(new_order.id))

    context = Context({
        'request' : request,
        'order_form' : order_form,
    })

    return HttpResponse(template.render(context))
