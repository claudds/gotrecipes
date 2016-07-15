from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^new/$', views.new_recipe, name='new_recipe'),
#	url(r'^login/$', 'django.contrib.auth.views.login'),
#	url(r'^logout/$, 'django.contrib.auth.views.logout'),
]