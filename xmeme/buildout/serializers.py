#for serializers

from rest_framework import serializers
from buildout.models import Memes

class MemesSerializer(serializers.ModelSerializer):

	class Meta:
		model = Memes
		#fields = ('name','employee_id')
		fields = '__all__'