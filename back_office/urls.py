from django.urls import path

from back_office.handlers import index
from back_office.handlers import customers
from back_office.handlers import documents
from back_office.handlers import employees
from back_office.handlers import orders
from back_office.handlers import passwords
from back_office.handlers import stock
from back_office.handlers import tasks

urlpatterns = [
    path('', index.index, name='back_office'),

    path('customers/', customers.customers, name='customers'),
    path('customers/<str:customer_id>/', customers.customer_profile, name='customer'),
    path('new_customer/', customers.new_customer, name='new_customer'),

    path('orders/', orders.orders, name='orders'),
    path('new_order/', orders.new_order, name='new_order'),
    path('new_order/<str:customer_id>', orders.new_order_by_customer, name='new_order_by_customer'),
    path('change_order/<str:order_id>', orders.change_order, name='change_order'),
    path('delete_order/<str:order_id>', orders.delete_order, name='delete_order'),

    path('stock/', stock.get_stock, name='stock'),

    path('employees/', employees.show_all_employees, name='employees'),
    path('new_employee/', employees.new_employee, name='new_employee'),
    path('change_employee/<str:employee_id>', employees.change_employee, name='change_employee'),
    path('delete_employee/<str:employee_id>', employees.delete_employee, name='delete_employee'),

    path('password/', passwords.password, name='password'),

    path('document/<str:document_id>', documents.view_document, name='view_document'),
    path('documents/', documents.get_documents, name='documents'),
    path('new_document/', documents.new_document, name='new_document'),
    path('edit_document/<str:document_id>', documents.edit_document, name='edit_document'),
    path('delete_document/<str:document_id>', documents.delete_document, name='delete_document'),

    path('tasks/', tasks.get_tasks, name='tasks'),
]
