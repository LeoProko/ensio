from django.urls import path

from landing.handlers import landing

urlpatterns = [
    path('<str:landing_id>', landing.index, name='index'),
]
