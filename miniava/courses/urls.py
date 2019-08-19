from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from miniava.courses import views
from miniava.courses.views import (index, details, enrollment, announcements, undo_enrollment, show_announcement, lessons, lesson, material)
urlpatterns = [ 
	url(r'^$', index, name='index'),
	url(r'^(?P<slug>[\w_-]+)/$', details, name='details'),
	url(r'^(?P<slug>[\w_-]+)/inscricao/$', enrollment, name='enrollment'),
	url(r'^(?P<slug>[\w_-]+)/anuncios/$', announcements, name='announcements'),
	url(r'^(?P<slug>[\w_-]+)/anuncios/(?P<pk>\d+)/$', show_announcement, name='show_announcement'),
	url(r'^(?P<slug>[\w_-]+)/cancelar-inscricao/$', undo_enrollment, name='undo_enrollment'),
	url(r'^(?P<slug>[\w_-]+)/aulas/$', lessons, name='lessons'),
	url(r'^(?P<slug>[\w_-]+)/aulas/(?P<pk>\d+)/$', lesson, name='lesson'),
	url(r'^(?P<slug>[\w_-]+)/materiais/(?P<pk>\d+)/$', material, name='material'),
]
