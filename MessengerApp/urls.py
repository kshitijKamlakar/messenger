"""MessengerApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from chat.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name = 'registration/login.html') ,name='login'),
    path('login/register/', signup ,name='login'),
    path('logout/', auth_views.auth_logout, name='logout'),
    path('redirect/', redirect ,name='login'),
    path('home/', index, name='index'),
    path('<str:room_name>/', room, name='room'),
]
