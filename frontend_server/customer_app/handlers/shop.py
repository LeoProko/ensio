from django.http import HttpResponse
from django.template import Template, Context
from django.utils import timezone
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from factory.html_factories.base import BaseHtmlFactory
from factory.models import Order, Item, ItemImage
from factory.forms import FastOrderForm

def index(request):
    template = Template(BaseHtmlFactory.create.customer_app(
        'Leo Proko shop', 'customer_app', 'shop', '', ''
    ))
    items = Item.objects.all()
    context = Context({
        'request' : request,
        'items' : items,
    })
    return HttpResponse(template.render(context))

def get_sizes_list(sizes) -> list:
    sizes_list = list()
    for size in sizes:
        sizes_list.append((size.size, size.size))
    return sizes_list

@csrf_exempt
def view_item(request, item_id):
    item = Item.objects.get(name_id=item_id)
    images = ItemImage.objects.filter(item=item)
    if request.user_agent.is_mobile:
        template = Template(BaseHtmlFactory.create.customer_app(
            item.name, 'customer_app', 'item_mobile', '', ''
        ))
    else:
        template = Template(BaseHtmlFactory.create.customer_app(
            item.name, 'customer_app', 'item', '', ''
        ))

    order_form = FastOrderForm(initial={
        'connection_type' : 'Phone',
    })
    order_form.fields['size'].choices = get_sizes_list(item.sizes.all())

    if request.method == 'POST':
        order_form = FastOrderForm(request.POST)
        order_form.fields['size'].choices = get_sizes_list(item.sizes.all())
        if order_form.is_valid():
            customer_name = order_form.cleaned_data['customer_name']
            connection_type = order_form.cleaned_data['connection_type']
            phone_number = order_form.cleaned_data['phone_number']
            size = order_form.cleaned_data['size']
            item = Item.objects.get(name_id=item_id)

            new_order = Order.objects.create(item=item,
                              customer_name=customer_name,
                              connection_type=connection_type,
                              phone_number=phone_number,
                              size=size,
                              date_created=timezone.now())
            new_order.save()

            print('New Order has been created', request.POST)
            return redirect('/track_order/' + str(new_order.id))

    context = Context({
        'request' : request,
        'item' : item,
        'images' : images,
        'order_form' : order_form,
    })
    return HttpResponse(template.render(context))
