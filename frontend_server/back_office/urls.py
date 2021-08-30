from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from back_office.handlers import index
from back_office.handlers import passwords

urlpatterns = [
    path('', index.index, name='back_office'),

    path('password/', passwords.password, name='password'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
