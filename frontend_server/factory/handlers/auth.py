from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group

from factory.html_factories.base import BaseHtmlFactory
from factory.forms import RegisterForm
from factory.decorators import unauthenticated_user

@csrf_exempt
@unauthenticated_user
def user_login(request):
    template = Template(BaseHtmlFactory.create.back_office(
        'Login', 'factory', 'login', '', ''
    ))
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/back_office/')
        messages.info(request, 'Email or password in incorrect')

    context = Context({
        'request' : request,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@unauthenticated_user
def user_register(request):
    template = Template(BaseHtmlFactory.create.back_office(
        'Register', 'factory', 'register', '', ''
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
