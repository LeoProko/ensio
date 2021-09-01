from django.http import HttpResponse
from django.template import Template, Context
from django.contrib.auth.decorators import login_required

from factory.html_factories.base import BaseHtmlFactory
from factory.decorators import allowed_users

@login_required(login_url='login')
@allowed_users(allowed_users_list=['cashier'])
def index(request):
    template = Template(BaseHtmlFactory.create.new_create(
        'crm', 'Index', ''
    ))
    context = Context({
        'request' : request,
    })
    return HttpResponse(template.render(context))
