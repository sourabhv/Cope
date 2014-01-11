from datetime import datetime

from django.db import models
from django.utils import timezone

class Book(models.Model):
	'''
	Part of accessing register enlisting book details.
	Contains general details relative to a book e.g. title, author,
	edition, publisher etc.
	'''
	# book info
	catalogueDate = models.DateField(auto_now_add=True, verbose_name=u'cataloguing date')
	title = models.CharField(max_length=100)
	edition = models.IntegerField(default=1)
	isbn = models.CharField(max_length=13, verbose_name=u'ISBN')
	ddc = models.CharField(max_length=3, verbose_name=u'DDC')
	bookNumber = models.CharField(max_length=)
	pages = models.IntegerField(blank=True)
	cost = models.IntegerField(blank=True)
	imageUrl = models.CharField(blank=True)

	# author and publisher info
	authors = models.CharField(max_length=100, blank=True)
	publisher = models.CharField(max_length=100)
	publishDate = models.DateField(null=True, blank=True)
	publishPlace = models.CharField(max_length=100, blank=True)

	# other info
	source = models.CharField(max_length=100, blank=True)
	remarks = models.TextField(blank=True)

	@property
	def copiesAvailable(self):
		pass

	@property
	def latestAvailableBy(self):
		pass

	def __init__(self, *args, **kwargs):
		super(Book, self).__init__(*args, **kwargs)
		if self.authors == '':
			self.authors = self.publisher

	def __unicode__(self):
		return self.title
