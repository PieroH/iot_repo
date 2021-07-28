from django.db import models
from django_celery_beat.models import PeriodicTask
# Create your models here.

from django.contrib.auth.models import User



class Reminder(models.Model):
    reminder_id = models.CharField(max_length=50, null=False)
    task = models.ForeignKey(PeriodicTask, on_delete = models.CASCADE, default="")
    message = models.TextField(null=False, verbose_name='Message', default="")
    author = models.ForeignKey(User, on_delete = models.CASCADE, default="")
    joke = models.BooleanField(default=False)
    weather = models.BooleanField(default=False)
    latitude = models.DecimalField(null=True, max_digits=8, decimal_places=5)
    longitude = models.DecimalField(null=True, max_digits=8, decimal_places=5)
