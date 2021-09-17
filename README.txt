Program Version 0.1(a)
------------------------------------------------
CS3450 Group 6 PuttPutt WebApplication 9/16/2021
------------------------------------------------


Project Managers:
	- David Rasmussen
	- Ethan Payne
	- Jonathan Crandall
	- Justin Reid

Usage Notes
----------------------------------------------------
- We've been tasked the purpose of building a WebApp to manage PuttPutt tournaments, and beverage orders from players/sponsors/managers from a local bar. Sponsors are able to choose a date for which they want to host a tournament, and the managers will have access to all the funds and stats of the specific tournament. Players are able to sign up for a tournament and enter a score at the end of their game. All users are able to order drinks from the Beverage Ordering System, and will be delivered to their desired hole. We've chosen to use Django as our base framework, allowing the website to be easily hosted and tested.
----------------------------------------------------


Version-Control
----------------------------------------------------
- We're using Git as our source code manager, and we all have access to the repot with permissions to modify.
----------------------------------------------------


Tool Stack
----------------------------------------------------
- Django Framework
- Git
- Asana
----------------------------------------------------

----------------------------------------------------

Installation Notes
----------------------------------------------------
- Django has built in functionality to run the server from the command line. To run the website, use the command "python manage.py runserver"
- If you want to use a specific IP address, this will need to be specified in DjangoFramework/settings.py under the IP section of code. To use the specific IP, use the same command before but with the desired IP and port "python manage.py runserver 192.168.0.1:8080"
----------------------------------------------------


Testing
----------------------------------------------------
- We will be using Python's standard library module unittest within our Django application.
Unit tests are run from the command line using the manage.py file, and the test key word.
Ex.
$ ./manage.py test

This runs all of the tests in the tests directory in our Django project. The python libraries makes creating tests and running them simple and non-complicated. 
----------------------------------------------------
