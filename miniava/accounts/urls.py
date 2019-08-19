from django.contrib import admin, auth
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf.urls import url, include
from miniava.accounts import views
from miniava.accounts.views import password_reset

urlpatterns = [
	url(r'^$', views.dashboard, name='dashboard'),
	url(r'^entrar/$', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
	url(r'^sair/$', auth_views.LogoutView.as_view(next_page="/"), name='logout'),
	url(r'^cadastre-se/$', views.register, name='register'),
	url(r'^nova-senha/$', views.password_reset, name='password_reset'),
	url(r'^confirmar-nova-senha/(?P<key>\w+)/$', views.password_reset_confirm, name='password_reset_confirm'),
	#url(r'^(?P<pk>\d+)/$', details, name='details'),
]
