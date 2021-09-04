from django.shortcuts import redirect
from django_hosts.resolvers import reverse

def index(request):
    return redirect(reverse('index', host='shop'))
