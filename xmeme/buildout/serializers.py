#for serializers

from rest_framework import serializers
from buildout.models import Memes #importing the Meme Model

class MemesSerializer(serializers.ModelSerializer): #creating the serializer

	class Meta:
		model = Memes
		#fields = ('name','employee_id')
		fields = '__all__'