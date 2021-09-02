from django.http import HttpResponse
from django.template import Template, Context
from django.contrib.auth.decorators import login_required
from django_hosts.resolvers import reverse

from factory.html_factories.base import BaseHtmlFactory
from factory.decorators import allowed_users

@login_required(login_url=reverse('login', host='base'))
def index(request):
    template = Template(BaseHtmlFactory.create.new_create(
        'crm', 'Index', ''
    ))
    context = Context({
        'request' : request,
    })
    return HttpResponse(template.render(context))
