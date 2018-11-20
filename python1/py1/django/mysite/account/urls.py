# -*- coding: utf-8 -*-
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = "account"

urlpatterns = [
    #path('login/', views.user_login, name='user_login'),
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'),name="user_login"),
    path('loginout/',auth_views.LogoutView.as_view(template_name='registration/loginout.html'),name="user_loginout"),
    path('register/',views.register,name="user_register"),
    path('password-change/',auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name="password_change"),
    #path('password-change-done/',auth_views.PasswordResetDoneView, name="password_change_done"),
]
