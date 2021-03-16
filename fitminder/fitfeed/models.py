from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from datetime import datetime

class Feed(models.Model):
	
	f1 = 'fa1'
	f2 = 'fa2'
	f3 = 'fa3'
	f4 = 'fa4'

	FIT_ACTIVITIES = [
		(f1, 'Fat Burn'),
		(f2, 'Cardio'),
		(f3, 'Strength'),
		(f4, '...')
	]

	title = models.CharField(max_length=100)
	content = models.CharField(
		max_length=3,
		choices=FIT_ACTIVITIES, 
		default=f4
	)
	duration = models.DurationField()
	datetime= models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	img = models.ImageField(default='#', upload_to='media')


	def __str__(self):
		return self.fit_title

	def was_published_recently(self):
		return self.datetime >= timezone.now() - datetime.timedelta(days=1)

	def get_absolute_url(self):
		return reverse('feed-feed', kwargs={'pk':self.pk})

	def save(self, **kwargs):
		super().save(**kwargs)
		img = Image.open(self.img.path)
		if img.height > 100 or img.width > 100:
			output_size = (100, 100)
			img.thumbnail(output_size)
			img.save(self.img.path)	