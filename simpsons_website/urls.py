"""simpsons_website URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.db import router

from django.urls import path
from django.views.generic import TemplateView

from simpsonapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^$', TemplateView.as_view(template_name='main_page.html'), name='home'),

    url(r'^characters$', views.Characters, name='characters'),
    url(r'^characters/(?P<characterid>[0-9]+)/$', views.Characters, name='character'),

    url(r'^contact$', views.contact, name='contact'),

    url(r'^login/$', views.login_view, name='login'),
    url(r'^signup/$', views.signup_view, name='signup'),
    url(r'^logout/$', views.logout_view, name='logout'),

    url(r'^introduction/$', views.introduction, name='introduction'),
]
