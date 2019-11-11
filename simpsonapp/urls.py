
from django.conf.urls import url

from simpsonapp import views

url(r'^characters$', views.character, name='characters'),
url(r'^characters/id=(?P<characterid>[0-9]+)/$', views.character, name='characters'),
