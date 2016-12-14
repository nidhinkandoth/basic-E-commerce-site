from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

class PostsSubmit(models.Model):
	title = models.CharField(max_length=100)
	text = models.TextField()
	product_image = models.ImageField(upload_to = 'pic_folder/')
	created_date = models.DateTimeField(default=timezone.now())

