"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.contrib import admin
from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView \
    , PasswordChangeView, PasswordChangeDoneView

import authentication.views
import blog.views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
        template_name='authentication/login.html', 
        redirect_authenticated_user=True, 
        next_page='home'
    ), name='login'),
    # path('', authentication.views.LoginPageView.as_view(), name='login'),
    # path('', authentication.views.login_page, name='login'),
    # path('logout/', authentication.views.logout_user, name='logout'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('password-change-done/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html'
    ), name='password-change-done'),
    path('password-change/', PasswordChangeView.as_view(
        template_name='authentication/password_change.html',
        success_url=reverse_lazy('password-change-done')
    ), name='password-change'),
    path('home/', blog.views.home, name='home'),
]
