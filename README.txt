Program Version 0.1(a)
------------------------------------------------
CS3450 Group 6 PuttPutt WebApplication 9/16/2021
------------------------------------------------


Project Managers:
	- David Rasmussen
	- Ethan Payne
	- Jonathan Crandall
	- Justin Reid


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


Installation Notes
----------------------------------------------------
- Django has built in functionality to run the server from the command line. To run the website, use the command 
	$ python manage.py runserver

- If you want to use a specific IP address, this will need to be specified in DjangoFramework/settings.py under the IP section of code. To use the specific IP, use the same command before but with the desired IP and port 
	$ python manage.py runserver 192.168.0.1:8080
--------------------------------------------------------------------------------------------------------


Organization:
----------------------------------------------------
	Code organization follows the general python and HTML standard programming guidelines. Using tabs, 
machine-friendly for variables, all caps for constants, and capitalized class names.
	Example:

		class User(models.Model):
		    user_id = models.CharField(max_length=14)

		    PLAYER = 'PL'
		    SPONSOR = 'SP'
		    MANAGER = 'MA'
		    DRINKMEISTER = 'DM'
		    USER_TYPE_CHOICES = [
			(PLAYER, 'Player'),
			(SPONSOR, 'Sponsor'),
			(MANAGER, 'Manager'),
			(DRINKMEISTER, 'DrinkMeister'),
		    ]
		    user_type = models.CharField(
			max_length = 2,
			choices = USER_TYPE_CHOICES,
			default = PLAYER
		    )

		    user_name = models.CharField(max_length=50)
		    password = models.CharField(max_length=21)
		    account_balance = models.FloatField(default=0)


Directory Map:
	CS3450_PUTTPUTT_GROUP^/DjangoFramework - Base Project, contains all files pertaining to the django framework
	CS3450_PUTTPUTT_GROUP^/DjangoFramework/PuttPutt - Contains all files pertaining to the webapp
	CS3450_PUTTPUTT_GROUP^/DjangoFramework/PuttPutt/templates - Contains all HTML template files
	CS3450_PUTTPUTT_GROUP^/DjangoFramework/PuttPutt/static - Contains all static files (.CSS, Resources, etc.)
----------------------------------------------------		


Testing:
----------------------------------------------------
- We will be using Python's standard library module unittest within our Django application.
Unit tests are run from the command line using the manage.py file, and the test key word.
Ex.
$ ./manage.py test

This runs all of the tests in the tests directory in our Django project. The python libraries makes creating tests and running them simple and non-complicated. 
----------------------------------------------------


System Testing:
--------------------------------------------------------------
	Database Debugging:
		We've included a page for database debugging to make sure we are creating instances of classes correctly.
	To test classes, run the site with the extension /drinkDemo.

		127.0.0.1/drinkDemo lists a few buttons where you can create instances of classes in the database. To make sure the
	changes were made, go to the site /admin page.

		127.0.0.1/admin page can be accessed ONLY by running the command 
			python manage.py createsuperuser
		and using your created user to sign in. 
