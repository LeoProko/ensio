from django.http import HttpResponse
from django.template import Template, Context
from django.contrib.auth.decorators import login_required

from frontend_server.html_factories.base import BaseHtmlFactory
from frontend_server.decorators import allowed_users

@login_required(login_url='login')
@allowed_users(allowed_users_list=[])
def index(request):
    template = Template(BaseHtmlFactory.create.back_office('Ensio', 'back_office/templates/', 'main', '', ''))
    context = Context({
        'request' : request,
    })
    return HttpResponse(template.render(context))