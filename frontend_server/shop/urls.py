from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500

from shop.handlers import shop
from factory.decorators import not_found

urlpatterns = [
    path('', shop.all_items, name='index'),
    path('item/<str:item_id>', shop.view_item, name='item'),
    path('track_order/', shop.track_order, name='track_oreder'),
    path('track_order/<str:order_id>', shop.track_order_by_id, name='track_oreder'),

    path('collections', shop.collections, name='collections'),
    path('delivery', shop.delivery, name='delivery'),
    path('contacts', shop.contacts, name='contacts'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = not_found
handler500 = not_found
