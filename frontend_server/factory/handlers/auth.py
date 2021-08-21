from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django_hosts.resolvers import reverse

from factory.html_factories.base import BaseHtmlFactory
from factory.forms import RegisterForm, LoginForm
from factory.decorators import unauthenticated_user

@csrf_exempt
@unauthenticated_user
def user_login(request):
    template = Template(BaseHtmlFactory.create.new_create(
        'factory', 'Login', 'login'
    ))
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('documents', host='docs'))

    context = Context({
        'request' : request,
        'form' : form,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@unauthenticated_user
def user_register(request):
    template = Template(BaseHtmlFactory.create.new_create(
        'factory', 'Register', 'register'
    ))
    form  = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = form.save(commit=False)
            user.public_name = username
            user.save()
            group = Group.objects.get(name='guest')
            user.groups.add(group)
            return redirect(reverse('documents', host='docs'))
    context = Context({
        'request' : request,
        'form' : form,
    })
    return HttpResponse(template.render(context))

def user_logout(request):
    logout(request)
    return redirect(reverse('login', host='base'))
