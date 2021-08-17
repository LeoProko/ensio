from django.urls import path

from customer_app.handlers import shop, track_order, help_pages
from back_office.handlers import documents

urlpatterns = [
    path('shop', shop.index, name='index'),
    path('shop/<str:item_id>', shop.view_item, name='item'),
    path('track_order/', track_order.track_order, name='track_oreder'),
    path('track_order/<str:order_id>', track_order.track_order_by_id, name='track_oreder'),
    path('collections', help_pages.collections, name='collections'),
    path('delivery', help_pages.delivery, name='delivery'),
    path('contacts', help_pages.contacts, name='contacts'),
    path('magazine', documents.get_documents, name='get_documents'),
]
