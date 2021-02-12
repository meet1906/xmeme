#this is for the apis that shall be created

from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from .serializers import *

class MemesList(APIView): #creating the class for api/memes endpoint which would serve get and post request for memes
	
	#get request
	def get(self,request):

		model = Memes.objects.all()
		serializer = MemesSerializer(model,many=True)
		return Response(serializer.data)

	#post request
	def post(self,request):

		#model = Users.objects.all()
		serializer = MemesSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #sending 400 Bad Request Status code in case meme couldn't be posted


class MemesListById(APIView): #creating the class for api/memes/<id> to help get the meme content via id

	def get(self,request,meme_id):

		meme=Memes.objects.get(meme_id=meme_id)
		serializer=MemesSerializer(meme)
		return Response(serializer.data)

	


