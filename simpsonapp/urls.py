
from django.conf.urls import url

from simpsonapp import views

url(r'^characters$', views.Characters, name='characters'),
url(r'^characters/(?P<characterid>[0-9]+)/$', views.Characters, name='characters'),
