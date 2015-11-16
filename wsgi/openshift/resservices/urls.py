from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from resservices import views

urlpatterns = patterns('',
	url(r'^api/$', views.RestaurantList.as_view()),
	url(r'^api/(?P<pk>[0-9]+)/$', views.RestaurantDetail.as_view()),
	url(r'^api/bookings/$', views.BookingList.as_view()),
	url(r'^api/bookings/(?P<pk>[0-9]+)/$', views.BookingDetail.as_view()),
	)
urlpatterns = format_suffix_patterns(urlpatterns)