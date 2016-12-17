from __future__ import unicode_literals
from django import forms
from django.db import models
import os.path
from django.utils import timezone
from PIL import Image
from cStringIO import StringIO
from django.core.files.uploadedfile import SimpleUploadedFile

class PostsSubmit(models.Model):
	title = models.CharField(max_length=100)
	text = models.TextField()
	product_image = models.ImageField(upload_to='pic_folder/')
	published_date = models.DateTimeField(blank = True, null = True)
	#image_height = models.IntegerField()
   	#image_width = models.IntegerField()
	thumbnail = models.ImageField(upload_to="thumbs/")
    	#thumbnail_height = models.IntegerField()
    	#thumbnail_width = models.IntegerField()
    	caption = models.CharField(max_length = 250, blank =True)
    
    	def __str__(self):
        	return "%s"%self.title
    
    	def __unicode__(self):
        	return self.title
        
    	def save(self, force_update=False, force_insert=False, thumb_size=(180,300)):

        	product_image = Image.open(self.product_image)
        
        	if product_image.mode not in ('L', 'RGB'):
            		product_image = product_image.convert('RGB')
            
        	# save the original size
        	self.product_image_width, self.product_image_height = product_image.size
        
        	product_image.thumbnail(thumb_size, Image.ANTIALIAS)
        
        	# save the thumbnail to memory
        	temp_handle = StringIO()
        	product_image.save(temp_handle, 'png')
        	temp_handle.seek(0) # rewind the file
        
        	# save to the thumbnail field
        	suf = SimpleUploadedFile(os.path.split(self.product_image.name)[-1],
                                 temp_handle.read(),
                                 content_type='image/png')
        	self.thumbnail.save(suf.name+'.png', suf, save=False)
        	self.thumbnail_width, self.thumbnail_height = product_image.size
        
        	# save the image object
        	super(PostsSubmit, self).save(force_update, force_insert)


	def publish(self):
        	self.published_date = timezone.now()
        	self.save()
