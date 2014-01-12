from django.conf.urls import patterns, include, url

urlpatterns = patterns('transactions.views',
	url(r'^$', 'index', name='index'),
)
