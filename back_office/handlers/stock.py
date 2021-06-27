from django.http import HttpResponse
from django.template import Template, Context
from django.contrib.auth.decorators import login_required

from frontend_server.html_factories.base import BaseHtmlFactory
from frontend_server.models import Item
from frontend_server.filters import ItemFilter
from frontend_server.decorators import allowed_users

@login_required(login_url='login')
@allowed_users(allowed_users_list=[])
def get_stock(request):
    template = Template(BaseHtmlFactory.create.back_office('Stock', 'back_office/templates/', 'stock', '', ''))

    items = Item.objects.all()
    items_count = items.count()
    filter = ItemFilter(request.GET, queryset=items)
    items = filter.qs

    context = Context({
        'request' : request,
        'items' : items,
        'filter' : filter,
        'items_count' : items_count,
    })
    return HttpResponse(template.render(context))
