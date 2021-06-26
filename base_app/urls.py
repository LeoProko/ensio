from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('back_office/', include('back_office.urls')),
    path('/', include('front_office.urls')),
]
