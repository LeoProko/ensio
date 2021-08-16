from django.http import HttpResponse
from django.template import Template, Context
from django.db.models import Q


from factory.html_factories.base import BaseHtmlFactory
from factory.models import Document
from factory.models import User

def index(request, username):
    user = User.objects.get(username=username)

    template = Template(BaseHtmlFactory.create.back_office(
        user.public_name, 'back_office', 'user_page', '', ''
    ))

    documents = Document.objects.filter(
        Q(is_link_public=True) &
        Q(is_indexed=True) & (
            Q(owner=user.public_name) |
            Q(authors__public_name__contains=user.public_name)
        )
    )

    context = Context({
        'documents' : reversed(documents),
        'documents_amount' : len(documents),
        'request' : request,
        'user' : user,
    })
    return HttpResponse(template.render(context))
