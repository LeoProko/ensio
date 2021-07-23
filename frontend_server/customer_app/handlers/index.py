from django.http import HttpResponse
from django.template import Template, Context
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from factory.html_factories.base import BaseHtmlFactory
from factory.decorators import allowed_users

def index(request):
    # template = Template(BaseHtmlFactory.create.customer_app('Ensio', 'customer_app/templates/', 'main', '', ''))
    # context = Context({
        # 'request' : request,
    # })
    # return HttpResponse(template.render(context))
    return redirect('/landing/ring_1')
