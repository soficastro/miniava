"""miniava URL Configuration

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
from django.conf.urls import url, include

from miniava.core import views
from miniava.core.views import home, contact
from miniava.courses import views
from miniava.courses.views import index
from miniava.forum import views
from miniava.forum.views import forumIndex
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('miniava.core.urls')),
    url(r'^conta/', include('miniava.accounts.urls')),
    url(r'^cursos/', include('miniava.courses.urls')),
    url(r'^forumIndex/', include('miniava.forum.urls')),
    #url(r'^$', home, name = 'home'),
    #url(r'^contato/$', contact, name = 'contact'),
    #url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
