from django.urls import path

from frontend_server.handlers import ensio_handler

from .models import *

urlpatterns = [
    path('', ensio_handler.index, name='index'),
    path('customers/', ensio_handler.customers, name='customers'),
    path('customers/<str:customer_id>/', ensio_handler.customer_profile, name='customer'),
    path('orders/', ensio_handler.orders, name='orders'),
    path('items/', ensio_handler.items, name='items'),
    path('employees/', ensio_handler.show_all_employees, name='employees'),
    path('new_employee/', ensio_handler.new_employee, name='new_employee'),
    path('change_employee/<str:employee_id>', ensio_handler.change_employee, name='change_employee'),
    path('delete_employee/<str:employee_id>', ensio_handler.delete_employee, name='delete_employee'),
    path('customers/', ensio_handler.customers, name='customers'),
    path('orders/', ensio_handler.orders, name='orders'),
    path('new_order/', ensio_handler.new_order, name='new_order'),
    path('new_order/<str:customer_id>', ensio_handler.new_order_by_customer, name='new_order_by_customer'),
    path('change_order/<str:order_id>', ensio_handler.change_order, name='change_order'),
    path('delete_order/<str:order_id>', ensio_handler.delete_order, name='delete_order'),
    path('password/', ensio_handler.password, name='password'),
]
