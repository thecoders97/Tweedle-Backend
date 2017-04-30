from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book(models.Model):
	book1 = models.CharField(max_length=100)
	city = models.CharField(max_length=50)
	author = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	library = models.CharField(max_length=100)

	def __str__(self):
		return '%s %s %s %s %s' % (self.book1,self.city,self.author,self.location,self.library)