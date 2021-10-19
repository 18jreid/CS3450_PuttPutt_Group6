from PuttPutt.models import User
from PuttPutt.models import Drink
from django import http
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.safestring import mark_safe

# Create your views here.
from django.views import generic
from .models import *
from .utils import Calendar


def index(request):
    return render(request, "PuttPutt/index.html")


def databaseDebugger(request):
    return render(request, "PuttPutt/databaseDebugger.html")


### This just reloads the same page you're on, but executes the print function inside the terminal.
def testButtonFunction(request):
    print("\n\nDebugger button pressed! This is where you will execute code for database debugging.\n\n")

    return HttpResponse("""<html><script>window.location.replace('/databaseDebugger');</script></html>""")


### Takes user to create user page
def createUserPage(request):
    print("\n\n Create a user! \n\n")

    return render(request, "PuttPutt/createUser.html")


### Takes user to create drink page
def createDrinkPage(request):
    print("\n\n Create a drink! \n\n")

    return render(request, "PuttPutt/createDrink.html")


### Takes user to drink demo
def drinkDemo(request):
    print("\n\n Drink Demo! \n\n")

    return render(request, "PuttPutt/drinkDemo.html")


### Creates user from input from the create user page
def createUser(request):
    user_name = request.POST['userName']
    password = request.POST['password']
    user_id = request.POST['userID']

    user = User()
    user.user_name = user_name
    user.password = password
    user.user_id = user_id
    user.account_balance = 500
    user.save()

    return HttpResponse("""<html><script>window.location.replace('/loginPage');</script></html>""")


### Creates drink from input from the create drink page
def createDrink(request):
    name = request.GET['name']
    description = request.GET['description']
    cost = request.GET['cost']

    drink = Drink()
    drink.name = name
    drink.description = description
    drink.cost = cost
    drink.save()

    return HttpResponse("""<html><script>window.location.replace('/drinkDemo');</script></html>""")


### Takes user to player dashboard
def playerDashboard(request):
    print("\n\n Player Dashboard! \n\n")

    return render(request, "PuttPutt/playerDashboard.html")

### Takes user to drinkmeister dashboard
def drinkmeisterDashboard(request):
    print("\n\n Drinkmeister Dashboard! \n\n")

    return render(request, "PuttPutt/drinkmeisterDashboard.html")

def sponsorDashboard(request):
    print("\n\n Sponsor Dashboard!\n\n")

    return render(request, "PuttPutt/sponsorDashboard.html")

### Takes user to manager dashboard
def managerDashboard(request):
    print("\n\n Manager Dashboard! \n\n")

    return render(request, "PuttPutt/managerDashboard.html")

### Takes user to login page
def loginPage(request):
    print("\n\n User Login page \n\n")

    return render(request, "PuttPutt/loginPage.html")


### Checks if user exists, and if their password is correct. If it is then they will go to the user dashboard
def signInUser(request):
    potentialUsers = User.objects.all().filter(user_id=request.POST['userID'])
    if (len(potentialUsers) != 0):
        user = User.objects.get(user_id=request.POST['userID'])

        if (user.password == request.POST['password']):
            return render(request, "PuttPutt/playerDashboard.html")
        else:
            return HttpResponse("Incorrect Password")

    else:
        return HttpResponse("User does not exist")


class CalendarView(generic.ListView):
    model = Tournament
    template_name = 'cal/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime.date(year, month, day=1)
    return datetime.today()
