from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from miniava.core import views
from miniava.core.views import home, contact#, index
urlpatterns = [
	url(r'^$', home, name = 'home'),
    url(r'^contato/$', contact, name = 'contact'),
    #url(r'^cursos/$', index, name = 'index')
]