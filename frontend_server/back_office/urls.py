from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from back_office.handlers import index
from back_office.handlers import documents
from back_office.handlers import orders
from back_office.handlers import passwords
from back_office.handlers import stock
from back_office.handlers import tasks
from back_office.handlers import user_page

urlpatterns = [
    path('', index.index, name='back_office'),

    path('orders/', orders.orders, name='orders'),
    path('change_order/<str:order_id>', orders.change_order, name='change_order'),
    path('delete_order/<str:order_id>', orders.delete_order, name='delete_order'),

    path('stock/', stock.get_stock, name='stock'),

    path('password/', passwords.password, name='password'),

    path('document/<str:document_id>', documents.view_document, name='view_document'),
    path('documents/', documents.get_documents, name='documents'),
    path('new_document/', documents.new_document, name='new_document'),
    path('edit_document/<str:document_id>', documents.edit_document, name='edit_document'),
    path('delete_document/<str:document_id>', documents.delete_document, name='delete_document'),

    path('tasks/', tasks.get_tasks, name='tasks'),

    path('user_page/<str:username>', user_page.index, name='user_page'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
