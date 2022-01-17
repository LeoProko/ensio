from django.urls import path
from django.conf.urls import handler404, handler500

from design.handlers import handler
from factory.decorators import not_found

urlpatterns = [
    path('', handler.index, name='index'),
    path('<str:image_name>', handler.generate_image_handler, name='generate_image_handler'),
]

handler404 = not_found
handler500 = not_found
