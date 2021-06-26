from django.urls import path

from customer_app.handlers import index

urlpatterns = [
    path('', index.index, name='index'),
]
