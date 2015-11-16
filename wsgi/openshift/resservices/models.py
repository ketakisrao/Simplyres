from django.db import models
import datetime
class Restaurant(models.Model):
	googlemaps_id = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	location = models.CharField(max_length=1000)
	def __str__(self):
		return self.name

class Booking(models.Model):
	restaurant = models.ForeignKey('Restaurant')
	username = models.CharField(max_length=100, default="ketakisrao")
	time = models.CharField(max_length=20)
	date = models.CharField(max_length=20)
	status = models.CharField(max_length=100)
	def __str__(self):
		return self.restaurant.name