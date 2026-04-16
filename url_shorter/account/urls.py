
from django.urls import path
from account import views

urlpatterns = [
    path('sign-in/', views.login, name="login_user"),
    path('sign-up/', views.register, name="register_user"),
    path('forget-password/', views.forgetpassword, name="forget_password"),
    path('verify-otp/', views.verify_otp, name="verify_otp"),
    
]
