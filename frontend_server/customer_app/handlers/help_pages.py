import os
from django.template import Template, Context
from django.http import HttpResponse
from django.conf import settings

from factory.html_factories.base import BaseHtmlFactory

def collections(request):
    template = Template(BaseHtmlFactory.create.customer_app(
        'Collections', 'customer_app', 'collections', '', ''
    ))
    images_path = 'static/img/collections/free_yourself'
    images = os.listdir(os.path.join(settings.BASE_DIR, images_path))
    images.sort()
    context = Context({
        'request' : request,
        'images' : images,
    })

    return HttpResponse(template.render(context))

def delivery(request):
    template = Template(BaseHtmlFactory.create.customer_app(
        'Delivery', 'customer_app', 'delivery', '', ''
    ))
    context = Context({
        'request' : request,
    })

    return HttpResponse(template.render(context))

def contacts(request):
    template = Template(BaseHtmlFactory.create.customer_app(
        'Contacts', 'customer_app', 'contacts', '', ''
    ))
    context = Context({
        'request' : request,
    })

    return HttpResponse(template.render(context))
