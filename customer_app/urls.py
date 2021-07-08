from django.urls import path

from customer_app.handlers import index, stock, track_order

urlpatterns = [
    path('', index.index, name='index'),
    path('item/<str:item_id>', stock.view_item, name='item'),
    path('track_order/', track_order.track_order, name='track_oreder'),
    path('track_order/<str:order_id>', track_order.track_order_by_id, name='track_oreder'),
]
