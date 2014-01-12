from django.conf.urls import patterns, include, url

urlpatterns = patterns('opac.views',
	url(r'^$', 'index', name='index'),
)
