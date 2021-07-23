from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import redirect
from django.forms import inlineformset_factory, modelformset_factory
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from factory.html_factories.base import BaseHtmlFactory
from factory.models import Task
from factory.forms import TaskForm
from factory.decorators import allowed_users

@csrf_exempt
@login_required(login_url='login')
@allowed_users(allowed_users_list=[])
def get_tasks(request):
    template = Template(BaseHtmlFactory.create.back_office('Tasks', 'back_office/templates/', 'tasks', '', ''))
    tasks = Task.objects.all()
    tasks_count = tasks.count()
    TaskFormSet = modelformset_factory(Task, form=TaskForm)
    task_form_set = TaskFormSet(queryset=tasks)
    if request.method == 'POST':
        for index, form in enumerate(task_form_set):
            print("index:::::::::", index, request.POST)
            form = TaskForm(request.POST, initial={
                'done' : request.POST.get('form-' + str(index) + '-done'),
                'task' : request.POST.get('form-' + str(index) + '-task'),
                'deadline' : request.POST.get('form-' + str(index) + '-deadline'),
                'chief' : request.POST.get('form-' + str(index) + '-chief'),
                'executors' : request.POST.get('form-' + str(index) + '-executors'),
            })
            form.save()
            if form.is_valid():
                form.save()

        return redirect('/tasks/')
        # for key, value in request.POST.items():
            # print("TASK REQUEST", key, value)
        # print("TASK RECEIVED", request.POST.get('form-1-done'))
        # task_form = TaskForm(request.POST)
        # if task_form.is_valid():
            # task_form.save()
            # return redirect('/tasks/')

    context = Context({
        'request' : request,
        'tasks' : tasks,
        'tasks_count' : tasks_count,
        'task_set' : task_form_set,
    })
    return HttpResponse(template.render(context))
