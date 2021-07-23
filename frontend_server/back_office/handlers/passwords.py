from django.http import HttpResponse
from django.template import Template, Context
from django.contrib.auth.decorators import login_required

from factory.html_factories.base import BaseHtmlFactory
from factory.models import Password
from factory.decorators import allowed_users


@login_required(login_url='login')
@allowed_users(allowed_users_list=[])
def password(request):
    passwords = Password.objects.all()
    passwords_count = passwords.count()
    template = Template(BaseHtmlFactory.create.back_office(
        'Passwords', 'back_office', 'passwords', '', ''
    ))
    context = Context({
        'request' : request,
        'passwords' : passwords,
        'passwords_count' : passwords_count,
    })
    return HttpResponse(template.render(context))
