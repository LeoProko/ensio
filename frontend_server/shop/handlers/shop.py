import os

from django.http import HttpResponse
from django.template import Template, Context
from django.utils import timezone
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from factory.html_factories.base import BaseHtmlFactory
from factory.logger import Logger
from crm.models import Order
from shop.models import Item, ItemImage, Tag
from crm.forms import FastOrderForm
from shop.forms import TrackOrderForm

logger = Logger(__name__, 'shop.leoproko.ru')

def all_items(request):
    template = Template(BaseHtmlFactory.create.new_create(
        'shop', 'Leo Proko Shop', 'all_items'
    ))
    items = Item.objects.all()
    is_mobile = False
    if request.user_agent.is_mobile:
        is_mobile = True
    context = Context({
        'request' : request,
        'items' : reversed(items),
        'is_mobile' : is_mobile,
    })
    logger.log_path(request)
    return HttpResponse(template.render(context))

def get_sizes_list(sizes) -> list:
    sizes_list = list()
    for size in sizes:
        sizes_list.append((size.size, size.size))
    return sizes_list

@csrf_exempt
def view_item(request, item_id: int):
    item = Item.objects.get(name_id=item_id)
    item_tags = [tag.name for tag in item.tags.all()]
    images = ItemImage.objects.filter(item=item)
    if request.user_agent.is_mobile:
        template = Template(BaseHtmlFactory.create.new_create(
            'shop', item.name, 'item_mobile'
        ))
    else:
        template = Template(BaseHtmlFactory.create.new_create(
            'shop', item.name, 'item'
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

    is_mobile = False
    if request.user_agent.is_mobile:
        is_mobile = True
    context = Context({
        'request' : request,
        'item' : item,
        'item_tags' : item_tags,
        'images' : images,
        'order_form' : order_form,
        'is_mobile' : is_mobile,
    })
    logger.log_path(request)
    return HttpResponse(template.render(context))

def collections(request):
    template = Template(BaseHtmlFactory.create.new_create(
        'shop', 'Collections', 'collections'
    ))
    images_path = 'static/img/shop/collections/free_yourself'
    images = os.listdir(os.path.join(settings.BASE_DIR, images_path))
    images.sort()
    is_mobile = False
    if request.user_agent.is_mobile:
        is_mobile = True
    context = Context({
        'request' : request,
        'images' : images,
        'is_mobile' : is_mobile,
    })
    logger.log_path(request)
    return HttpResponse(template.render(context))

def delivery(request):
    template = Template(BaseHtmlFactory.create.new_create(
        'shop', 'Delivery', 'delivery'
    ))
    is_mobile = False
    if request.user_agent.is_mobile:
        is_mobile = True
    context = Context({
        'request' : request,
        'is_mobile' : is_mobile,
    })
    logger.log_path(request)
    return HttpResponse(template.render(context))

def contacts(request):
    template = Template(BaseHtmlFactory.create.new_create(
        'shop', 'Contacts', 'contacts'
    ))
    is_mobile = False
    if request.user_agent.is_mobile:
        is_mobile = True
    context = Context({
        'request' : request,
        'is_mobile' : is_mobile,
    })
    logger.log_path(request)
    return HttpResponse(template.render(context))

@csrf_exempt
def track_order(request):
    template = Template(BaseHtmlFactory.create.new_create(
        'shop', 'Track Order', 'track_order'
    ))
    form = TrackOrderForm()
    if request.method == 'POST':
        form = TrackOrderForm(request.POST)
        if form.is_valid():
            order_id = form.cleaned_data['order_id']
            return redirect('/track_order/' + order_id)
    is_mobile = False
    if request.user_agent.is_mobile:
        is_mobile = True
    context = Context({
        'request' : request,
        'form' : form,
        'is_mobile' : is_mobile,
    })
    logger.log_path(request)
    return HttpResponse(template.render(context))



def track_order_by_id(request, order_id):
    template = Template(BaseHtmlFactory.create.new_create(
        'shop', 'Track Order', 'track_order_by_id'
    ))
    order_is_found = True
    order = ''
    try:
        order = Order.objects.get(id=order_id)
    except:
        order_is_found = False
    is_mobile = False
    if request.user_agent.is_mobile:
        is_mobile = True
    context = Context({
        'request' : request,
        'order_is_found' : order_is_found,
        'order' : order,
        'is_mobile' : is_mobile,
    })
    logger.log_path(request)
    return HttpResponse(template.render(context))
