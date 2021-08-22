from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500

from docs.handlers import docs
from docs.handlers import user_page
from factory.decorators import not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', docs.get_all, name='documents'),
    path('document/<str:document_id>', docs.get_doc, name='view_document'),
    path('new/', docs.new_doc, name='new_document'),
    path('edit/<str:document_id>', docs.edit_doc, name='edit_document'),
    path('remove/<str:document_id>', docs.remove_doc, name='remove_document'),

    path('user/<str:username>', user_page.index, name='user_page'),
]

handler404 = not_found
handler500 = not_found
