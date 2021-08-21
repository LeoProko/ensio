from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from shop.handlers import shop
from shop.handlers import stock
from shop.handlers import orders

urlpatterns = [
    path('', shop.index, name='index'),
    path('item/<str:item_id>', shop.view_item, name='item'),
    path('track_order/', shop.track_order, name='track_oreder'),
    path('track_order/<str:order_id>', shop.track_order_by_id, name='track_oreder'),

    path('collections', shop.collections, name='collections'),
    path('delivery', shop.delivery, name='delivery'),
    path('contacts', shop.contacts, name='contacts'),

    path('orders/', orders.orders, name='orders'),
    path('change_order/<str:order_id>', orders.change_order, name='change_order'),
    path('remove_order/<str:order_id>', orders.remove_order, name='remove_order'),

    path('stock/', stock.get_stock, name='stock'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
