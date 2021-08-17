from functools import reduce

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

    if request.user.is_authenticated:
        if request.user.is_superuser:
            documents = Document.objects.filter(
                Q(is_link_public=True) &
                    Q(owner=user.public_name) |
                    Q(authors__public_name__contains=user.public_name)
                )
            )
        else:
            documents = Document.objects.filter(
                (
                    Q(owner=user.public_name) |
                    Q(authors__public_name__contains=user.public_name)
                ) & (
                        (
                            Q(is_link_public=True) &
                            Q(is_indexed=True)
                        ) |
                        reduce(
                            lambda x, y : x | y,
                            [Q(groups__name__contains=user_group.name)
                            for user_group in request.user.groups.all()]
                        )
                    ) |
                    Q(owner=request.user.username) |
                    Q(authors__public_name__contains=request.user.public_name)
                )
            ).distinct()
    else:
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
