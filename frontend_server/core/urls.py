from django.contrib import admin
from django.urls import include, path
from django.conf.urls import handler404, handler500

from factory.decorators import not_found

urlpatterns = [
    path('', include('factory.urls')),
    path('admin/', admin.site.urls),
]

handler404 = not_found
handler500 = not_found
