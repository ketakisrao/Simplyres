from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required
import datetime
from resservices.models import Restaurant, Booking

def home(request):
     return render_to_response('home/home.html')



@login_required
def dashboard(request):
	username = None
	if request.user.is_authenticated():
		username = request.user.username
	now = datetime.datetime.now()
	date_today = now.strftime("%Y-%m-%d")
	if request.method == 'GET':
		return render(request, 'home/dashboard.html', {'username' : username, 'date' : date_today})
	elif request.method == 'POST':
		if request.POST:
			try:
				r = Restaurant.objects.get(googlemaps_id=request.POST['gmaps_id'])
			except Restaurant.DoesNotExist:
				r = Restaurant(googlemaps_id=request.POST['gmaps_id'], name=request.POST['place_name'], location=request.POST['location'])
				r.save()
			b = Booking(username=username,
			 date=datetime.datetime.strptime(request.POST['date'], "%Y-%m-%d").date(),
			 time=datetime.datetime.strptime(request.POST['time'], "%H:%M").time(),
			 status="Confirmed")
			b.restaurant = r
			b.save()
			b_arr = Booking.objects.filter(username=username)
			return render(request, 'home/displaybookings.html', {'bookings': b_arr})


@login_required
def bookings(request):
	if request.user.is_authenticated():
		username = request.user.username
		b_arr = Booking.objects.filter(username=username)
	return render(request, 'home/displaybookings.html', {'bookings': b_arr})	
