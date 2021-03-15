from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class FitProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	img = models.ImageField(default="profile.jpg", upload_to="media/fit_profile_pic")

	def __str__(self):
		return f'{self.user.username} Profile'

