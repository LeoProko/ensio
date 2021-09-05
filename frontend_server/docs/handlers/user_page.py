from functools import reduce

from django.http import HttpResponse
from django.template import Template, Context
from django.db.models import Q

from factory.html_factories.base import BaseHtmlFactory
from docs.models import Document
from factory.models import User

def index(request, username):
    user = User.objects.get(username=username)

    template = Template(BaseHtmlFactory.create.new_create(
        'docs', user.public_name, 'user_page'
    ))

    if request.user.is_authenticated:
        if request.user == user:
            documents = Document.objects.filter(
                Q(owner=user.username) |
                Q(authors__username__contains=user.username) |
                (
                    reduce(
                        lambda x, y : x | y,
                        [Q(groups__name__contains=user_group.name)
                        for user_group in request.user.groups.all()]
                    ) &
                    Q(is_link_public=True)
                )
            ).distinct()
        elif request.user.is_superuser:
            documents = Document.objects.filter(
                (
                    Q(owner=user.username) |
                    Q(authors__username__contains=user.username)
                ) &
                Q(is_link_public=True)
            ).distinct()
        else:
            documents = Document.objects.filter(
                (
                    Q(owner=user.username) |
                    Q(authors__username__contains=user.username)
                ) & (
                        (
                            Q(is_link_public=True) &
                            Q(is_indexed=True)
                        ) |
                        reduce(
                            lambda x, y : x | y,
                            [Q(groups__name__contains=user_group.name)
                            for user_group in request.user.groups.all()]
                        ) |
                        Q(owner=request.user.username) |
                        Q(authors__username__contains=request.user.username)
                    )
            ).distinct()
    else:
        documents = Document.objects.filter(
            (
                Q(owner=user.username) |
                Q(authors__username__contains=user.username)
            ) &
            Q(is_link_public=True) &
            Q(is_indexed=True)
        )

    context = Context({
        'documents' : reversed(documents),
        'documents_amount' : len(documents),
        'request' : request,
        'user' : user,
    })
    return HttpResponse(template.render(context))
