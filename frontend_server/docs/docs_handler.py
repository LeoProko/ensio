from functools import reduce
from markdown import markdown

from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django_hosts.resolvers import reverse

from factory.html_factories.base import BaseHtmlFactory
from docs.models import Document
from django.contrib.auth.models import Group
from docs.forms import DocumentForm
from factory.decorators import allowed_users, no_permissions


@login_required(login_url=reverse('login', host='base'))
def get_all(request):
    template = Template(BaseHtmlFactory.create.new_create(
        'docs', 'Documents', 'documents'
    ))
    documents = []
    if request.user.is_authenticated:
        if request.user.is_superuser:
            documents = Document.objects.filter(
                Q(is_link_public=True) |
                Q(owner=request.user.username) |
                reduce(
                    lambda x, y : x | y,
                    [Q(groups__name__contains=user_group.name)
                    for user_group in request.user.groups.all()]
                )
            ).distinct()
        else:
            documents = Document.objects.filter(
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
                Q(authors__public_name__contains=request.user.public_name)
            ).distinct()

    context = Context({
        'documents' : reversed(documents),
        'request' : request,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@login_required(login_url=reverse('login', host='base'))
@allowed_users(allowed_users_list=['cashier'])
def new_doc(request):
    template = Template(BaseHtmlFactory.create.new_create(
        'docs', 'New doc', 'new_document'
    ))
    document_form = DocumentForm()

    if request.method == 'POST':
        document_form = DocumentForm(request.POST)
        if document_form.is_valid():
            form = document_form.save(commit=False)
            form.owner = request.user.username
            form.html_data = markdown(form.markdown_data, extensions=['fenced_code'])
            form.save()
            document_form.save_m2m()
            print('New document has been created', request.POST)
            return redirect(reverse('edit_document', str(form.id), host='docs'))

    context = Context({
        'request' : request,
        'form' : document_form,
        'footer' : True,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@login_required(login_url=reverse('login', host='base'))
def edit_doc(request, document_id):
    template = Template(BaseHtmlFactory.create.new_create(
        'docs', 'Editor', 'new_document'
    ))
    document = Document.objects.get(id=document_id)
    document_form = DocumentForm(instance=document)
    if request.method == 'POST':
        document_form = DocumentForm(request.POST, instance=document)
        if document_form.is_valid():
            form = document_form.save(commit=False)
            form.html_data = markdown(form.markdown_data, extensions=['fenced_code'])
            form.save()
            document_form.save_m2m()
            print('Document', document_id, 'has been changed', request.POST)
            return redirect(reverse('edit_document', document_id, host='docs'))

    context = Context({
        'request' : request,
        'document' : document,
        'form' : document_form,
        'footer' : True,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
def get_doc(request, document_id):
    try:
        document = Document.objects.get(id=document_id)
    except:
        return no_permissions(request)

    if not document.is_link_public:
        if request.user.is_authenticated:
            name = str(request.user.username)
            if name != document.owner:
                if request.user.is_superuser:
                    return no_permissions(request)
                if name not in map(
                        lambda author : author.username,
                        document.authors.all()
                    ):
                    return no_permissions(request)
        else:
            return no_permissions(request)

    template = Template(BaseHtmlFactory.create.new_create(
        'docs', document.title, 'document'
    ))

    can_edit = False
    if request.user.is_authenticated:
        can_edit = request.user.username in document.authors.all()
        can_edit |= request.user.username == document.owner
        can_edit |= request.user.is_superuser

    context = Context({
        'request' : request,
        'document' : document,
        'can_edit' : can_edit,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@login_required(login_url=reverse('login', host='base'))
def remove_doc(request, document_id):
    template = Template(BaseHtmlFactory.create.new_create(
        'docs', 'Remove doc', 'remove_document'
    ))
    document = Document.objects.get(id=document_id)
    if request.method == 'POST':
        document.delete()
        return redirect(reverse('documents', host='docs'))

    context = Context({
        'request' : request,
        'document' : document,
    })
    return HttpResponse(template.render(context))
