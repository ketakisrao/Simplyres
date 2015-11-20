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


##### If you wish to access features like Login with Facebook or Twitter please use the Openshift site as the features will not work on your local machines.
