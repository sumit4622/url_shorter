
from django.urls import path, include
from account import views

urlpatterns = [
    path('sign-in/', views.login, name="login_user"),
    path('sign-up/', views.register, name='register_user'),
]
