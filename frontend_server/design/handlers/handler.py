from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django_hosts.resolvers import reverse

from factory.html_factories.base import BaseHtmlFactory
from design.src.image_generator import generate_image
from design.forms import HandelForm


@csrf_exempt
def index(request):
    template = Template(BaseHtmlFactory.create.new_create(
        'design', 'Image generator', 'main'
    ))
    form = HandelForm()
    if request.method == 'POST':
        form = HandelForm(request.POST)
        if form.is_valid():
            image_name = form.cleaned_data['image_name']
            return redirect(reverse('generate_image_handler', [image_name], host='design'))

    context = Context({
        'request' : request,
        'form' : form,
    })
    return HttpResponse(template.render(context))

def generate_image_handler(request, image_name):
    template = Template(BaseHtmlFactory.create.new_create(
        'design', 'Image generator', 'image_generator'
    ))
    image_path = generate_image(image_name)
    context = Context({
        'request' : request,
        'image_path' : image_path,
        'image_name' : image_name,
    })
    return HttpResponse(template.render(context))

