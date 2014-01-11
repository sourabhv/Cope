from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def authHandler(request):
	if request.user.is_authenticated():
		# use opac.views.index
		pass
	else:
		# use transactions.views.index
		pass


