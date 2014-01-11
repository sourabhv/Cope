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

class BookCopy(models.Model):
	date = models.DateField(auto_now_add=True, verbose_name=u'cataloguing date')
	bookCopyNumber = models.CharField(verbose_name=u'book copy number')
	issued = models.BooleanField(default=False)
	lastIssueDate = models.DateField(verbose_name=u'last issue date', null=True, blank=True)

	# Foreign keys
	book_category = models.ForeignKey(Book, related_name='copies')
	issued_to = models.ForeignKey(EndUser, related_name='issued_books',
		null=True, blank=True, default=None)

	class Meta:
		verbose_name=u'book copy'
		verbose_name_plural=u'book copies'

	def __unicode__(self):
		return '%s | %s' % (self.book_category.title, self.bookCopyNumber)

class EndUser(models.Model):
	'''
	Part of accessing register enlisting EndUser details.
	Inherited by Student and Employee Models.

	Contains common user specific details - name, card_number, gender,
	phone_number.
	'''

	genderChoices = (
		(u'F', u'Female'),
		(u'M', u'Male'),
		(u'U', u'Unspecified'),
	)

	name = models.CharField(max_length=100)
	cardNumber = models.CharField(max_length=100)
	gender = models.CharField(max_length=1, choices=genderChoices)
	phoneNumber = models.CharField(max_length=20)

	def __unicode__(self):
		return '%s | %s' % (self.name, self.cardNumber)
