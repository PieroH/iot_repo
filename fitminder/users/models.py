from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class FitProfile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	img = models.ImageField(default="profile.png", upload_to="media")

	def __str__(self):
		return f'{self.user.username} FitProfile'

	def save(self, **kwargs):
		super().save(**kwargs)
		img = Image.open(self.img.path)
		if img.height > 100 or img.width > 100:
			output_size = (100, 100)
			img.thumbnail(output_size)
			img.save(self.img.path)	

