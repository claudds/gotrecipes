from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^new/$', views.new_recipe, name='new_recipe'),
	url(r'^recipe/(?P<pk>\d+)/$', views.recipe_detail, name='recipe_detail'),
	url(r'^recipe/(?P<pk>\d+)/edit/$', views.recipe_edit, name='recipe_edit'),
	url(r'^recipe/(?P<pk>\d+)/remove/$', views.recipe_delete, name='recipe_delete'),
]
