from rest_framework import serializers
from .models import Restaurant, Booking

class RestaurantSerializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		field = ('id', 'name')

class BookingSerializer(serializers.ModelSerializer):
	restaurant = RestaurantSerializer
	class Meta:
		model = Booking
		field= ('id')