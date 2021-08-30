from django.http import HttpResponse
from django.template import Template, Context
from django.contrib.auth.decorators import login_required

from factory.html_factories.base import BaseHtmlFactory
from shop.models import Item
from factory.filters import ItemFilter
from factory.decorators import allowed_users

@login_required(login_url='login')
@allowed_users(allowed_users_list=[])
def get_stock(request):
    template = Template(BaseHtmlFactory.create.back_office(
        'Stock', 'back_office', 'stock', '', ''
    ))
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
