from django.conf.urls import url

from .views import (
	hidrometros_list,
	hidrometros_create,
	hidrometros_detail,
	hidrometros_update,
	hidrometros_delete,
	hidrometros_home,
	)

urlpatterns = [
	#url(r'^$', hidrometros_list, name='list'),
	url(r'^dados/(?P<local>[\w\-]+)/$', hidrometros_list, name='list'),
	url(r'^$', hidrometros_home, name='home'),
    url(r'^create/$', hidrometros_create, name='create'),
    url(r'^(?P<id>\d+)/$', hidrometros_detail, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', hidrometros_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', hidrometros_delete, name='delete'),

]
