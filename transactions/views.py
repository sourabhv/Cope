from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
	if request.user.is_authenticated():
		return HttpResponse('Hi! Authenticated User.')
	else:
		return HttpResponseRedirect(reverse('opac:index'))
