from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

class PostsSubmit(models.Model):
	title = models.CharField(max_length=100)
	text = models.TextField()
	product_image = models.ImageField()
	published_date = models.DateTimeField(blank = True, null = True)

def publish(self):
        self.published_date = timezone.now()
        self.save()
def __str__(self):
	return self.title
