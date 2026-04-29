"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include
from django.shortcuts import redirect, render


def index(request):
    return redirect('authors:login')

def no_permission(request):
    return render(request, 'marmitas/pages/no_permission.html')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index),
    path('sem-permissao/', no_permission),
    path('auth/', include('authors.urls')),
    path('marmitas/', include('marmitas.urls')),
]