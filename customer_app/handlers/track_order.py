from django.http import HttpResponse
from django.template import Template, Context
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

from frontend_server.html_factories.base import BaseHtmlFactory
from frontend_server.forms import TrackOrderForm
from frontend_server.models import Order

@csrf_exempt
def track_order(request):
    template = Template(BaseHtmlFactory.create.empty(
        'Track Order', 'customer_app/templates/', 'track_order', 'track_order', ''))

    form = TrackOrderForm()

    if request.method == 'POST':
        form = TrackOrderForm(request.POST)
        if form.is_valid():
            order_id = form.cleaned_data['order_id']
            return redirect('/track_order/' + order_id)


    context = Context({
        'request' : request,
        'form' : form,
    })
    return HttpResponse(template.render(context))



def track_order_by_id(request, order_id):
    template = Template(BaseHtmlFactory.create.empty(
        'Track Order', 'customer_app/templates/', 'track_order_by_id', 'track_order_by_id', ''))
    order_is_found = True
    order = ''
    try:
        order = Order.objects.get(id=order_id)
    except:
        order_is_found = False
    context = Context({
        'request' : request,
        'order_is_found' : order_is_found,
        'order' : order,
    })
    return HttpResponse(template.render(context))
