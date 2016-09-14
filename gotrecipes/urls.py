from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^new/$', views.new_recipe, name='new_recipe'),
	url(r'^search/$', views.search_recipe, name='search_recipe'),
	url(r'^search_result/(?P<st>\w+)/$', views.search_result, name='search_result'),
	url(r'^recipe/(?P<pk>\d+)/$', views.recipe_detail, name='recipe_detail'),
	url(r'^recipe/(?P<pk>\d+)/edit/$', views.recipe_edit, name='recipe_edit'),
	url(r'^recipe/(?P<pk>\d+)/remove/$', views.recipe_delete, name='recipe_delete'),
]
