from django.http import HttpResponse
from django.template import Template, Context

from frontend_server.html_factories.base import BaseHtmlFactory
from frontend_server.models import Item

def view_item(request, item_id):
    item = Item.objects.get(id=item_id)
    template = Template(BaseHtmlFactory.create.customer_app(item.name, 'customer_app/templates/', 'item', '', ''))
    context = Context({
        'request' : request,
        'item': item,
    })
    return HttpResponse(template.render(context))
