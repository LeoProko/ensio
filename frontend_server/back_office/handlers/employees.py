from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from factory.html_factories.base import BaseHtmlFactory
from factory.models import Employee
from factory.forms import EmployeeForm
from factory.decorators import allowed_users

@login_required(login_url='login')
@allowed_users(allowed_users_list=[])
def show_all_employees(request):
    employees = Employee.objects.all()
    status_count = {
        'works' : employees.filter(status='Works').count(),
        'on_holiday' : employees.filter(status='On holiday').count(),
        'dismissed' : employees.filter(status='Dismissed').count(),
    }
    employees_count = employees.count()
    template = Template(BaseHtmlFactory.create.back_office(
        'Employees', 'back_office', 'employees', '', ''
    ))
    context = Context({
        'request' : request,
        'employees': employees,
        'employees_count': employees_count,
        'status_count': status_count,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@login_required(login_url='login')
@allowed_users(allowed_users_list=[])
def new_employee(request):
    template = Template(BaseHtmlFactory.create.back_office(
        'New employee', 'back_office', 'new_employee', '', ''
    ))
    employee_form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            print('New employee has been created', request.POST)
            return redirect('/employees/')

    context = Context({
        'request' : request,
        'form' : employee_form,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@login_required(login_url='login')
@allowed_users(allowed_users_list=[])
def change_employee(request, employee_id):
    template = Template(BaseHtmlFactory.create.back_office(
        'Change employee', 'back_office', 'new_employee', '', ''
    ))
    employee = Employee.objects.get(id=employee_id)
    employee_form = EmployeeForm(instance=employee)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            print('Employee', employee_id, 'has been changed', request.POST)
            return redirect('/employees/')

    context = Context({
        'request' : request,
        'form' : employee_form,
    })
    return HttpResponse(template.render(context))

@csrf_exempt
@login_required(login_url='login')
@allowed_users(allowed_users_list=[])
def delete_employee(request, employee_id):
    template = Template(BaseHtmlFactory.create.back_office(
        'Delete employee', 'back_office', 'delete_employee', '', ''
    ))
    employee = Employee.objects.get(id=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('/employees/')

    context = Context({
        'request' : request,
        'employee' : employee,
    })
    return HttpResponse(template.render(context))
