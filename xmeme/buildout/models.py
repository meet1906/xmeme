from django.db import models

# Create your models here.
class Memes(models.Model):
	name = models.CharField(max_length=1000)
	caption = models.CharField(max_length=1000)
	url = models.URLField(max_length=10000)


	def __str__(self):
		return f"{self.name} - {self.caption}"
	

