"""python_B67 URL Configuration

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
from django.contrib import admin
from django.urls import path
from Vapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Hello),
    path('india/',views.India),
    path('gujarat/',views.Gujarat),
    path('maharastra/',views.Maharastra),
    path('karnataka/',views.Karanataka),
    path('gandhinagar/',views.Gandhi),
    path('mumbai/',views.Mumbai),
    path('bengluru/',views.Bengaluru),
    path('australia/',views.Australia),
    path('america/',views.America),
    path('cal/',views.California),
    path('florida/',views.Florida),
    path('geo/',views.Geo),
]
