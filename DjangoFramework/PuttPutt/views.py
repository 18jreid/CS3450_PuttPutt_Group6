from PuttPutt.models import Drink
from django import http
from datetime import datetime
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, logout

# Create your views here.
from django.views import generic
from .models import *


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


### Creates drink from input from the create drink page
def createDrink(request):
    name = request.POST['name']
    description = request.POST['description']
    cost = request.POST['cost']

    drink = Drink()
    drink.name = name
    drink.description = description
    drink.cost = cost
    drink.save()

    return redirect("managerDashboard")


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

def manageUsers(request):
    users = User.objects.all()
    for user in users:
        print(user)
    context = {
        'users' : users
    }
    print("\n\n Manage Users page \n\n")

    return render(request, "PuttPutt/manageUsers.html", context)


### Checks if user exists, and if their password is correct. If it is then they will go to the user dashboard
def signInUser(request):
    userName = request.POST['userID']
    password = request.POST['password']

    myUser = authenticate(username=userName, password=password)

    if (myUser is not None):
        auth.login(request=request, user=myUser)

        if (myUser.profile.user_type == "PL"):
            return redirect('playerDashboard')
        elif (myUser.profile.user_type == "SP"):
            return redirect('sponsorDashboard')
        elif (myUser.profile.user_type == "MA"):
            return redirect('managerDashboard')
        elif (myUser.profile.user_type == "DM"):
            return redirect('drinkmeisterDashboard')
    else:
        context = {
            'error' : "Username or Password is incorrect"
        }
        return render(request, "PuttPutt/loginPage.html", context)

def login(request):
    if (request.user.is_authenticated):
        return redirect('playerDashboard')
    else:
        return render(request, "PuttPutt/loginPage.html")

def logout_user(request):
    auth.logout(request)

    return redirect('index')


### Creates user from input from the create user page
def createUser(request):
    user_name = request.POST['userID']
    email = request.POST['email']
    emailConfirmation = request.POST['emailConfirmation']
    first_name = request.POST['firstName']
    last_name = request.POST['lastName']
    password = request.POST['password']
    passwordConfirmation = request.POST['passwordConfirmation']

    return checkSignUpFields(request, user_name, first_name, last_name, email, emailConfirmation, password, passwordConfirmation)


def checkSignUpFields(request, userName, firstName, lastName, email, emailConfirmation, password, passwordConfirmation):
    context = {}
    if (firstName == ""):
        print("\n \n FIRST NAME IS EMPTY \n \n ")
        context = {
            'error' : "First name is empty"
        }
        return render(request, "PuttPutt/createUser.html", context)

    if (lastName == ""):
        print("\n \n LAST NAME IS EMPTY \n \n")
        context = {
            'error' : "Last name is empty"
        }
        return render(request, "PuttPutt/createUser.html", context)

    if (userName == ""):
        print("\n \n USERNAME IS EMPTY \n \n")
        context = {
            'error' : "Username is empty"
        }
        return render(request, "PuttPutt/createUser.html", context)

    if (email == ""):
        print("\n \n EMAIL IS EMPTY \n \n ")
        context = {
            'error' : "Email is empty"
        }
        return render(request, "PuttPutt/createUser.html", context)

    if (emailConfirmation == ""):
        print("\n \n EMAIL CONFIRMATION IS EMPTY \n \n ")
        context = {
            'error' : "Email confirmation is empty"
        }
        return render(request, "PuttPutt/createUser.html", context)

    if (password == ""):
        print("\n \n  PASSWORD IS EMPTY \n \n ")
        context = {
            'error' : "Password is empty"
        }
        return render(request, "PuttPutt/createUser.html", context)

    if (passwordConfirmation == ""):
        print("\n \n PASSWORD CONFIRMATION IS EMPTY\n \n ")
        context = {
            'error' : "Password Confirmation is empty"
        }
        return render(request, "PuttPutt/createUser.html", context)

    if (email != emailConfirmation):
        print("\n \n EMAILS DO NOT MATCH")
        context = {
            'error' : "Emails don't match"
        }
        return render(request, "PuttPutt/createUser.html", context)
    
    if (password != passwordConfirmation):
        print("\n \n PASSWORDS DO NOT MATCH \n \n")
        context = {
            'error' : "Passwords do not match"
        }
        return render(request, "PuttPutt/createUser.html", context)

    userObjects =  User.objects.all()

    for user in userObjects:
        if (user.username == userName):
            context = {
                'error': "User already exists"
            }
            print("\n \n USER ALREADY EXISTS \n \n")
            return render(request, "PuttPutt/createUser.html", context)

        if (user.email == email):
            context = {
                'error': "Email has already been used"
            }
            print("\n \n EMAIL HAS ALREADY BEEN USED \n \n")
            return render(request, "PuttPutt/createUser.html", context)

    user = User.objects.create_user(userName, email, password)
    user.first_name = firstName
    user.last_name = lastName
    user.save()
    
    return render(request, "PuttPutt/loginPage.html")
