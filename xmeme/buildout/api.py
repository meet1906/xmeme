#this is for the apis that shall be created

from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from .serializers import *

class MemesList(APIView):

	def get(self,request):

		model = Memes.objects.all()
		serializer = MemesSerializer(model,many=True)
		return Response(serializer.data)

	def post(self,request):

		#model = Users.objects.all()
		serializer = MemesSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



