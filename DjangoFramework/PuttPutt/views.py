from PuttPutt.models import User
from PuttPutt.models import Drink
from django import http
from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render


# Create your views here.
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
    user_name = request.GET['userName']
    password = request.GET['password']
    user_id = request.GET['userID']

    user = User()
    user.user_name = user_name
    user.password = password
    user.user_id = user_id
    user.account_balance = 500
    user.save()

    return HttpResponse("""<html><script>window.location.replace('/drinkDemo');</script></html>""")

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