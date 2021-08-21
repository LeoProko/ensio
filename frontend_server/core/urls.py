from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('back_office/', include('back_office.urls')),
    path('', include('factory.urls')),
    path('admin/', admin.site.urls),
]
