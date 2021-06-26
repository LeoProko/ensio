from django.urls import path

from frontend_server.handlers import auth

urlpatterns = [
    path('login/', auth.user_login, name='login'),
    path('register/', auth.user_register, name='register'),
    path('logout/', auth.user_logout, name='logout'),
]
