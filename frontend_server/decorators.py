from django.shortcuts import redirect
from django.template import Template, Context
from django.http import HttpResponse

from frontend_server.html_factories.base import BaseHtmlFactory

def no_permissions(request):
    template = Template(BaseHtmlFactory.create('No permissions', 'frontend_server/templates/', 'no_permissions', '', ''))
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
            return no_permissions(request)
        return wrapper
    return decorator
