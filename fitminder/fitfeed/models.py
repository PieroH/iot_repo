from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from datetime import datetime



i1 = '..1'
i2 = '..2'
i3 = '..3'
i4 = '..4'

FIT_INTENSITY = [
	(i1, 'LOW'),
	(i2, 'MODERATE'),
	(i3, 'HIGH'),
	(i4, '...')
]

class Feed(models.Model):
	

	title = models.CharField(max_length=100)
	intensity = models.CharField(
		max_length=3,
		choices=FIT_INTENSITY, 
		default=i4
	)
	preparation = models.CharField(max_length=400, default="")
	instruction = models.CharField(max_length=600, default="")
	duration = models.DurationField(null=False)
	datetime = models.DateTimeField(default=timezone.now)
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