from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('transactions:index'))
	else:
		return HttpResponse('Hi! Anonymous User.')
