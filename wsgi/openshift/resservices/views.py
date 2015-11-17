from django.http import HttpResponse
from django.shortcuts import render
from serializers import *
from .models import *
from rest_framework import generics
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class RestaurantList(generics.ListCreateAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantSerializer
	def post(self, request, format=None):
		serializer = RestaurantSerializer(data=request.data)
		print "I got here %s", request.data
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantSerializer

#For Bookings

class BookingList(generics.ListCreateAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer
	@csrf_exempt
	def post(self, request, format=None):
		serializer = BookingSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer

