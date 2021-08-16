from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from markdown import markdown

from factory.html_factories.base import BaseHtmlFactory
from factory.models import Document
from factory.forms import DocumentForm
from factory.decorators import allowed_users, no_permissions

def get_documents(request):
    template = Template(BaseHtmlFactory.create.back_office(
        'Documents', 'back_office', 'documents', '', ''
    ))
    if request.user.is_authenticated:
        if request.user.is_superuser:
            documents = Document.objects.filter(
                Q(is_link_public=True) |
                Q(owner=request.user.public_name)
            )
        else:
            documents = Document.objects.filter(
                Q(is_link_public=True) & (
                    Q(is_indexed=True) |
                    Q(groups__in=request.user.groups.all())
                ) |
                Q(owner=request.user.public_name)
            )
    else:
        documents = Document.objects.filter(
            is_indexed=True,
            is_link_public=True,
        )

    context = Context({
        'documents' : reversed(documents),
        'request' : request,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@login_required(login_url='login')
@allowed_users(allowed_users_list=['cashier'])
def new_document(request):
    template = Template(BaseHtmlFactory.create.back_office(
        'New document', 'back_office', 'new_document', '', ''
    ))
    document_form = DocumentForm()

    if request.method == 'POST':
        document_form = DocumentForm(request.POST)
        if document_form.is_valid():
            form = document_form.save(commit=False)
            form.owner = request.user.public_name
            form.html_data = markdown(form.markdown_data)
            form.save()
            document_form.save_m2m()
            print('New document has been created', request.POST)
            return redirect('/back_office/edit_document/' + str(form.id))

    context = Context({
        'request' : request,
        'form' : document_form,
    })
    return HttpResponse(template.render(context))

from django.contrib.auth.models import Group

@csrf_exempt
@login_required(login_url='login')
def edit_document(request, document_id):
    template = Template(BaseHtmlFactory.create.back_office(
        'Edit document', 'back_office', 'new_document', '', ''
    ))
    document = Document.objects.get(id=document_id)
    document_form = DocumentForm(instance=document)
    if request.method == 'POST':
        document_form = DocumentForm(request.POST, instance=document)
        if document_form.is_valid():
            form = document_form.save(commit=False)
            form.groups.add(Group.objects.get(name='superuser'))
            form.html_data = markdown(form.markdown_data)
            form.save()
            document_form.save_m2m()
            print('Document', document_id, 'has been changed', request.POST)
            return redirect('/back_office/edit_document/' + document_id)

    context = Context({
        'request' : request,
        'document' : document,
        'form' : document_form,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
def view_document(request, document_id):
    try:
        document = Document.objects.get(id=document_id)
    except:
        return no_permissions(request)

    if not document.is_link_public:
        if request.user.is_authenticated:
            name = str(request.user.public_name)
            if name != document.owner and\
                    name not in map(
                        lambda author : author.public_name,
                        document.authors.all()):
                return no_permissions(request)
        else:
            return no_permissions(request)

    template = Template(BaseHtmlFactory.create.back_office(
        document.title, 'back_office', 'document', '', ''
    ))

    can_edit = False
    if request.user.is_authenticated:
        can_edit = request.user.public_name in document.authors.all()
        can_edit |= request.user.public_name == document.owner
        can_edit |= request.user.is_superuser

    context = Context({
        'request' : request,
        'document' : document,
        'can_edit' : can_edit,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@login_required(login_url='login')
def delete_document(request, document_id):
    template = Template(BaseHtmlFactory.create.back_office(
        'Remove document', 'back_office', 'delete_document', '', ''
    ))
    document = Document.objects.get(id=document_id)
    if request.method == 'POST':
        document.delete()
        return redirect('/back_office/documents/')

    context = Context({
        'request' : request,
        'document' : document,
    })
    return HttpResponse(template.render(context))
