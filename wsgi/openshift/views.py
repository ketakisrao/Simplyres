from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required

def home(request):
     return render_to_response('home/home.html')
@login_required
def dashboard(request):
	username = None
	if request.user.is_authenticated():
		username = request.user.username
	return render(request, 'home/dashboard.html', {'username' : username})