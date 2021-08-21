from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from docs import docs_handler

from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', docs_handler.get_all, name='documents'),
    path('<str:document_id>', docs_handler.get_doc, name='view_document'),
    path('new/', docs_handler.new_doc, name='new_document'),
    path('edit/<str:document_id>', docs_handler.edit_doc, name='edit_document'),
    path('remove/<str:document_id>', docs_handler.remove_doc, name='remove_document'),
]
