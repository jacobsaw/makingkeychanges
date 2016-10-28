from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

class Publication(models.Model):
	date = models.CharField(max_length=1000)
	date_order = models.DateField(default=timezone.now)
	title = models.CharField(max_length=1000)
	link_title = models.CharField(max_length=1000)
	link = models.CharField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return 'Publication: ' + self.title

class Previous_Engagements(models.Model):
	role = models.CharField(max_length=1000)
	date = models.CharField(max_length=1000)
	date_order = models.DateField(default=timezone.now)
	description = models.CharField(max_length=2000)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return self.date + ' ' + self.description
