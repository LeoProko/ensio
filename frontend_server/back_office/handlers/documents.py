from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from markdown import markdown

from factory.html_factories.base import BaseHtmlFactory
from factory.models import Document
from factory.forms import DocumentForm
from factory.decorators import allowed_users

@login_required(login_url='login')
@allowed_users(allowed_users_list=[])
def get_documents(request):
    template = Template(BaseHtmlFactory.create.back_office('Documents', 'back_office/templates/', 'documents', '', ''))
    documents = Document.objects.all()
    documents_count = documents.count()
    context = Context({
        'documents' : documents,
        'documents_count' : documents_count,
        'request' : request,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@login_required(login_url='login')
@allowed_users(allowed_users_list=['cashier'])
def new_document(request):
    template = Template(BaseHtmlFactory.create.back_office('New document', 'back_office/templates/', 'new_document', '', ''))
    document_form = DocumentForm(initial={'owner':request.user})

    if request.method == 'POST':
        document_form = DocumentForm(request.POST)
        if document_form.is_valid():
            form = document_form.save(commit=False)
            form.html_data = markdown(form.markdown_data)
            form.save()
            print('New document has been created', request.POST)
            return redirect('/documents/')

    context = Context({
        'request' : request,
        'form' : document_form,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@login_required(login_url='login')
@allowed_users(allowed_users_list=[])
def edit_document(request, document_id):
    template = Template(BaseHtmlFactory.create.back_office('Document', 'back_office/templates/', 'new_document', '', ''))
    document = Document.objects.get(id=document_id)
    document_form = DocumentForm(instance=document)
    if request.method == 'POST':
        document_form = DocumentForm(request.POST, instance=document)
        if document_form.is_valid():
            form = document_form.save(commit=False)
            form.html_data = markdown(form.markdown_data)
            form.save()
            print('Document', document_id, 'has been changed', request.POST)
            return redirect('/edit_document/' + document_id)

    context = Context({
        'request' : request,
        'document' : document,
        'form' : document_form,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@login_required(login_url='login')
@allowed_users(allowed_users_list=[])
def view_document(request, document_id):
    template = Template(BaseHtmlFactory.create.back_office('Document', 'back_office/templates/', 'document', '', ''))
    document = Document.objects.get(id=document_id)
    context = Context({
        'request' : request,
        'document' : document,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@login_required(login_url='login')
@allowed_users(allowed_users_list=[])
def delete_document(request, document_id):
    template = Template(BaseHtmlFactory.create.back_office('Remove document', 'back_office/templates/', 'delete_document', '', ''))
    document = Document.objects.get(id=document_id)
    if request.method == 'POST':
        document.delete()
        return redirect('/documents/')

    context = Context({
        'request' : request,
        'document' : document,
    })
    return HttpResponse(template.render(context))
