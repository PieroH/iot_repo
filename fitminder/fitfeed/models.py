from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from datetime import datetime



class Event(models.Model):
    event_name = models.CharField(max_length=50, null=False)
    start_date = models.DateField('Event starts', blank=False, default = timezone.now)
    start_time = models.TimeField('Time', blank=False, default = timezone.now)
    end_date = models.DateField('Event ends', blank=False, default = timezone.now)
    end_time = models.TimeField('Ends at', blank=False, default = timezone.now)
    date_published = models.DateTimeField(default = timezone.now)
    description = models.TextField(null=False, verbose_name='Description', default="Description Here")
    location = models.CharField(max_length=100, null=False, default="")
    author = models.ForeignKey(User, on_delete = models.CASCADE, default="")

    def was_published_recently(self):
        return self.date_published >= timezone.now() - datetime.timedelta(days=1)

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk':self.pk})
