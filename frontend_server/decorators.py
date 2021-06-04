from django.http import HttpResponse
from django.shortcuts import redirect

from frontend_server.handlers import ensio_handler

def unauthenticated_user(handle_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return handle_func(request, *args, **kwargs)
    return wrapper

def allowed_users(allowed_users=[]):
    allowed_users.append('superuser')
    def decorator(handle_func):
        def wrapper(request, *args, **kwargs):
            for group in request.user.groups.all():
                if group.name in allowed_users:
                    return handle_func(request, *args, **kwargs)
            return ensio_handler.no_permissions(request)
        return wrapper
    return decorator
