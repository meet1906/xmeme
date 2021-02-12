from django.db import models
import uuid



# Creating my Model - Memes here which would have meme_id,name,caption and url.
class Memes(models.Model):
	#meme_id is for unique memes content which would contain the unique uuid that django creates.This shall be helpful for our search meme content through meme_id as well
	meme_id = models.UUIDField(default=uuid.uuid4) 

	#name is for meme-owner
	name = models.CharField(max_length=1000)

	#caption is for meme-caption
	caption = models.CharField(max_length=1000)

	#url is for meme image URL which you see is a URL Field so it automatically validates a URL and sends a bad request if the url ain't proper 
	url = models.URLField(max_length=10000)


	def __str__(self):
		return f"{self.name} - {self.caption}" #this is just for localhost or server/admin so that I can see the content through name and caption and not uuids
	

