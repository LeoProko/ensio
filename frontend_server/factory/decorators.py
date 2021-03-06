from django.shortcuts import redirect
from django.template import Template, Context
from django.http import HttpResponse

from factory.html_factories.base import BaseHtmlFactory

def not_found(request, *args, **kwargs):
    template = Template(BaseHtmlFactory.create.new_create(
        'factory', 'Not found', 'not_found'
    ))
    context = Context({
        'request' : request,
    })
    return HttpResponse(template.render(context))

def unauthenticated_user(handle_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return handle_func(request, *args, **kwargs)
    return wrapper

def allowed_users(allowed_users_list=[]):
    allowed_users_list.append('superuser')
    def decorator(handle_func):
        def wrapper(request, *args, **kwargs):
            for group in request.user.groups.all():
                if group.name in allowed_users_list:
                    return handle_func(request, *args, **kwargs)
            return not_found(request)
        return wrapper
    return decorator
