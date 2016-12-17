from django.db import models

# Create your models here. 

class picture(models.Model):
	name = models.CharField(max_length=64)
	location = models.CharField(max_length=64)
	subject = models.CharField(max_length=64)
	camera = models.CharField(max_length=32, default='Olympus')
	image = models.ImageField()
	description = models.TextField()
	date = models.DateField('date taken')
	
	def __str__(self):
		title = 'Title: %s' % (self.name)
		title += '\nCamera: %s ' % (self.camera)
		return title