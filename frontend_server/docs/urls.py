from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from docs.handlers import docs
from docs.handlers import user_page

from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', docs.get_all, name='documents'),
    path('<str:document_id>', docs.get_doc, name='view_document'),
    path('new/', docs.new_doc, name='new_document'),
    path('edit/<str:document_id>', docs.edit_doc, name='edit_document'),
    path('remove/<str:document_id>', docs.remove_doc, name='remove_document'),

    path('user/<str:username>', user_page.index, name='user_page'),
]
