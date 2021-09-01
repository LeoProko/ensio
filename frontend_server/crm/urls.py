from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500

from crm.handlers import crm
from crm.handlers import orders
from factory.decorators import not_found

urlpatterns = [
    path('', crm.index, name='index'),

    path('orders/', orders.orders, name='orders'),
    path('change_order/<str:order_id>', orders.change_order, name='change_order'),
    path('remove_order/<str:order_id>', orders.remove_order, name='remove_order'),
]

handler404 = not_found
handler500 = not_found
