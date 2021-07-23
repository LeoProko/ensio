from django.http import HttpResponse
from django.template import Template, Context

from factory.html_factories.base import BaseHtmlFactory
from factory.models import Item

def view_item(request, item_id):
    item = Item.objects.get(id=item_id)
    template = Template(BaseHtmlFactory.create.customer_app(
        item.name, 'customer_app', 'item', '', ''
    ))
    context = Context({
        'request' : request,
        'item': item,
    })
    return HttpResponse(template.render(context))

def view_items(request):
    template = Template(BaseHtmlFactory.create.customer_app(
        'Leo Proko shop', 'customer_app', 'items', 'items', ''
    ))
    items = Item.objects.all()
    context = Context({
        'request' : request,
        'items' : items,
    })
    return HttpResponse(template.render(context))
