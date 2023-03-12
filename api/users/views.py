from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.hashers import check_password

from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import User
from .serializers import UserSerializer

# Register new user
class UserSignUpView(APIView):
	def post(self, request):
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'status': 201,
				'messages': 'user has been created'})
		else:
			return Response({'status': 403, 'message': 'email already exists'})
