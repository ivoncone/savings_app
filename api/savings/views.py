from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from savings.models import Savings

from savings.serializers import SavingsSerializer, DaysSerializer

class DaysView(APIView):
	def post(self, request):
		data = request.data
		serializer = DaysSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response({'status': 201,
				'message': 'your savings seection has been save',
				'data': serializer.data})
		else:
			return Response({'status': 400, 
				'message': 'you have to choose a number between 7 and 365'})

# Create savings view per user
class SavingsView(APIView):

	def get(self, request):
		savings = Savings.objects.all()
		serializer = SavingsSerializer(savings, many=True)
		number = Savings.numbers
		for n in number:
			total = sum(n)
		print(total)
		return Response({'status': 200, 'data': serializer.data})


	def post(self, request):
		data = request.data
		serializer = SavingsSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response({'status': 201,
				'message': 'daily saving has been save',
				'data': serializer.data
				})
		else:
			return Response({'status': 400, 
				'message': 'service unavilable'})