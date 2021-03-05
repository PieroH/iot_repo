from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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

	fit_title = models.CharField(max_length=100)
	fit_content = models.CharField(
		max_length=3,
		choices=FIT_ACTIVITIES, 
		default=f4
	)
	fit_duration = models.DurationField()
	datetime_feed = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	fit_image = models.ImageField(default='#', upload_to='activity_thumbnail')


	def __str__(self):
		return self.title