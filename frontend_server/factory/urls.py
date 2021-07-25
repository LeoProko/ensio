from django.urls import path

from factory.handlers import auth, index

urlpatterns = [
    path('', index.index, name='index'),
    path('login/', auth.user_login, name='login'),
    path('register/', auth.user_register, name='register'),
    path('logout/', auth.user_logout, name='logout'),
]
