"""autobot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from botapp import views as bot_views
from adminapp import views as admin_views
from userapp import views as user_views
from superadmin import views as superadmin_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bot_views.index),
    path('admin-login/', admin_views.adminLogin),
    path('admin-validate/', admin_views.adminLoginValidate),
    path('adminIn/', admin_views.adminIn),
    path('upload-image/', admin_views.index),
    path('addcrime/', admin_views.addCrime),
    path('admin-logout/', admin_views.adminOut),
    path('number-validate/', admin_views.numberValidate),
    path('user-login/', user_views.userLogin),
    path('user-validate/', user_views.userLoginValidate),
    path('userIn/', user_views.userIn),
    path('sadmin-login/', superadmin_views.sadminLogin),
    path('sadmin-validate/', superadmin_views.sadminLoginValidate),
    path('sadminIn/', superadmin_views.sadminIn),
    path('sadmin-logout/', superadmin_views.sadminOut),
]
