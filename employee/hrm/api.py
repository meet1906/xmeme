#this is for creating apis

from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from .serializers import *

class UserList(APIView):

	def get(self,request):

		model = Users.objects.all()
		serializer = UsersSerializer(model,many=True)
		return Response(serializer.data)

	def post(self,request):

		#model = Users.objects.all()
		serializer = UsersSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



