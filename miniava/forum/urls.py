from django.conf.urls import include, url
from miniava.forum import views
from miniava.forum.views import forumIndex, thread, reply_correct, reply_incorrect
urlpatterns = [
    url(r'^$', forumIndex, name='forumIndex'),
    url(r'^tag/(?P<tag>[\w_-]+)/$', forumIndex, name='forumIndex_tagged'),
    url(r'^respostas/(?P<pk>\d+)/correta/$', reply_correct, name='reply_correct'),
    url(r'^respostas/(?P<pk>\d+)/incorreta/$', reply_incorrect, name='reply_incorrect'),
    url(r'^(?P<slug>[\w_-]+)/$', thread, name='thread'),
]