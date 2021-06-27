from django.urls import path

from customer_app.handlers import index, stock

urlpatterns = [
    path('', index.index, name='index'),

    path('item/<str:item_id>', stock.view_item, name='item'),
]
