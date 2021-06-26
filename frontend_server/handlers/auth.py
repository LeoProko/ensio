from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group

from frontend_server.html_factories.base import BaseHtmlFactory
from frontend_server.forms import RegisterForm
from frontend_server.decorators import unauthenticated_user

@csrf_exempt
@unauthenticated_user
def user_login(request):
    template = Template(BaseHtmlFactory.create_back_office('Login', 'frontend_server/templates/', 'login', '', ''))
    context = Context({
        'request' : request,
    })
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/back_office/')
        messages.info(request, 'Username or password in incorrect')
    return HttpResponse(template.render(context))

@csrf_exempt
@unauthenticated_user
def user_register(request):
    template = Template(BaseHtmlFactory.create_back_office('Register', 'frontend_server/templates/', 'register', '', ''))
    form  = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            group = Group.objects.get(name='guest')
            user.groups.add(group)
            messages.success(request, username + ' has been registered')
            return redirect('/back_office/')

    context = Context({
        'request' : request,
        'form' : form
    })
    return HttpResponse(template.render(context))

def user_logout(request):
    logout(request)
    return redirect('login')

def no_permissions(request):
    template = Template(BaseHtmlFactory.create_back_office('No permissions', 'frontend_server/templates/', 'no_permissions', '', ''))
    context = Context({
        'request' : request,
    })
    return HttpResponse(template.render(context))
