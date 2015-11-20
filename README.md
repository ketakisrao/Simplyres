Simply Res!
===========
SimplyRes allows you to make reservations at restaurants, SimplyReserve!


This application is built on Django -- A python based web framework. The backend used is SqLite3 and the site has been deployed on Openshift (Red Hat Cloud) at [SimplyRes](https://simplyres-ketakisrao.rhcloud.com "SimplyRes!").


If you want a copy of this application up and running on your local machines, do the following:


+ Make a folder and cd into it.
+ Clone the repository using git clone https://github.com/ketakisrao/Simplyres.git
+ cd to simplyres/
+ Install the app using python setup.py install
+ To run this application cd wsgi/openshift/ and then python manage.py runserver
+ Simplyres! should now be running on http://localhost:8080/


##### If you wish to access features like Login with Facebook or Twitter please use the Openshift site as the features will not work on your local machines. Please use a HTML5 compatible browser for the application since it contains a few elements from HTML5.


After Installation
==================


+ Visit the homepage and click on GetStarted
+ Login/Register/Login with Facebook or Twitter to be able to see your dashboard and make bookings.
+ Search for a restaurant on the google maps input provided. (Maps has been integrated for user convenience and interactivity)
+ Choose number of people (cannot be greater than 16).
+ Choose a date and timing for the booking.
+ Hit Book! to confirm the booking
+ Navigate to the bookings tab to be able to view your bookings.
