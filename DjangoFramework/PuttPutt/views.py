from PuttPutt.models import Drink
from django import http
from datetime import datetime
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, logout
from datetime import date

# Create your views here.
from django.views import generic
from .models import *

# Takes user to the adds funds page
def addFunds(request):
    print("\n\n Add Funds page! \n\n")

    return render(request, "PuttPutt/addFunds.html")

# Adds funds to the users account
def addMoney(request):
    amount = request.POST['amount']
    request.user.profile.account_balance = request.user.profile.account_balance + int(amount)
    request.user.profile.save()

    return redirect('playerDashboard')

# Takes user to create user page
def createUserPage(request):
    print("\n\n Create a user! \n\n")

    return render(request, "PuttPutt/createUser.html")


# Takes user to create drink page
def createDrinkPage(request):
    print("\n\n Create a drink! \n\n")

    return render(request, "PuttPutt/createDrink.html")

# Creates drink from input from the create drink page
def createDrink(request):
    name = request.POST['name']
    description = request.POST['description']
    cost = request.POST['cost']

    drink = Drink()
    drink.name = name
    drink.description = description
    drink.cost = cost
    drink.save()

    return redirect("manageDrinks")

# Creates user from input from the create user page
def createUser(request):
    user_name = request.POST['userID']
    email = request.POST['email']
    emailConfirmation = request.POST['emailConfirmation']
    first_name = request.POST['firstName']
    last_name = request.POST['lastName']
    password = request.POST['password']
    passwordConfirmation = request.POST['passwordConfirmation']

    return checkSignUpFields(request, user_name, first_name, last_name, email, emailConfirmation, password, passwordConfirmation)

# Takes user to current tournament page
def currentTournament(request):
    tournaments = Calendar.objects.all()
    context = {
        'tournaments' : tournaments
    }

    for t in tournaments:
        if (t.date == date.today()):
            print("THERES A TOURNAMENT TODAY!")
            todaysTourney = t.date
            prizePool = t.prize_pool
            players = Tournament.objects.all().filter(date=date.today())
            
            context = {
                'prizePool' : prizePool,
                'todaysTourney' : todaysTourney,
                'players' : players
            }

            for player in players:
                user = str(request.user)
                
                
                print(user == player.user_id)
                if (user == player.user_id):
                    isPlaying = True
                    context = {
                        'prizePool' : prizePool,
                        'todaysTourney' : todaysTourney,
                        'isPlaying' : isPlaying,
                        'players' : players
                    }
    
    print("\n\n Current Tournament! \n\n")

    return render(request, "PuttPutt/currentTournament.html", context)

# Checks the sign up fields on the sign up page
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

# Takes user to database debugger page
def databaseDebugger(request):
    return render(request, "PuttPutt/databaseDebugger.html")
    
# Takes user to drink demo
def drinkDemo(request):
    print("\n\n Drink Demo! \n\n")

    return render(request, "PuttPutt/drinkDemo.html")

# Takes user to drinkmeister dashboard
def drinkmeisterDashboard(request):
    print("\n\n Drinkmeister Dashboard! \n\n")

    if (request.user.profile.user_type == "PL"):
        return redirect("playerDashboard")
    elif (request.user.profile.user_type == "SP"):
        return redirect('sponsorDashboard')
    elif (request.user.profile.user_type == "MA"):
        return redirect('managerDashboard')
    elif (request.user.profile.user_type == "DM"):
        return render(request, "PuttPutt/drinkmeisterDashboard.html")

# Takes user to index page (AKA Main page)
def index(request):
    tournaments = Calendar.objects.all()
    context = {
        'tournaments' : tournaments
    }

    for t in tournaments:
        if (t.date == date.today()):
            todaysTourney = t

            newTournaments = Calendar.objects.all().exclude(date=t.date)

            players = Tournament.objects.all().filter(date=date.today())

            context = {
                'tournaments' : newTournaments,
                'todaysTourney' : todaysTourney,
                'players' : players
            }
    

    return render(request, "PuttPutt/index.html", context)

# Signs up user for the tournament that day
def joinTournament(request):
    tournament = Tournament()
    tournament.user_id = request.user
    tournament.save()

    return redirect('playerDashboard')

# Takes user to login page
def loginPage(request):
    print("\n\n User Login page \n\n")

    return render(request, "PuttPutt/loginPage.html")

# Checks if the user is logged in already, if not it returns them to login page
def login(request):
    if (request.user.is_authenticated):
        return redirect('playerDashboard')
    else:
        return render(request, "PuttPutt/loginPage.html")

# Logs user out of their account
def logout_user(request):
    auth.logout(request)

    return redirect('index')

# Takes user to manager dashboard
def managerDashboard(request):
    print("\n\n Manager Dashboard! \n\n")

    if (request.user.profile.user_type == "PL"):
        return redirect("playerDashboard")
    elif (request.user.profile.user_type == "SP"):
        return redirect('sponsorDashboard')
    elif (request.user.profile.user_type == "MA"):
        return render(request, "PuttPutt/managerDashboard.html")
    elif (request.user.profile.user_type == "DM"):
        return redirect('drinkmeisterDashboard')

# Takes manager to manage current tournament page
def manageCurrentTournament(request):
    print("\n\n Manage Current Tournament page! \n\n")
    tournaments = Calendar.objects.all()
    context = {
        'tournaments' : tournaments
    }

    for t in tournaments:
        if (t.date == date.today()):
            todaysTourney = t
            prizePool = t.prize_pool
            players = Tournament.objects.all().filter(date=date.today())
            
            context = {
                'todaysTourney' : todaysTourney,
                'players' : players
            }

    return render(request, "PuttPutt/manageCurrentTournament.html", context)

# Takes user to the manage users page
def manageUsers(request):
    users = User.objects.all()
    for user in users:
        print(user)
    context = {
        'users' : users
    }
    print("\n\n Manage Users page \n\n")

    return render(request, "PuttPutt/manageUsers.html", context)

# Takes user to the manage users page
def manageDrinks(request):
    drinks = Drink.objects.all()
    for drink in drinks:
        print(drink)
    context = {
        'drinks' : drinks
    }
    print("\n\n Manage Drinks page \n\n")

    return render(request, "PuttPutt/manageDrinks.html", context)

# Takes user to the order drinks page
def orderDrinks(request):
    print("\n\n Order Drinks page! \n\n")

    return render(request, "PuttPutt/orderDrinks.html")

# Takes user to player dashboard page
def playerDashboard(request):
    print("\n\n Player Dashboard! \n\n")

    if (request.user.profile.user_type == "PL"):
        return render(request, "PuttPutt/playerDashboard.html")
    elif (request.user.profile.user_type == "SP"):
        return redirect('sponsorDashboard')
    elif (request.user.profile.user_type == "MA"):
        return redirect('managerDashboard')
    elif (request.user.profile.user_type == "DM"):
        return redirect('drinkmeisterDashboard')

# Takes user to player scoresheet page
def scoresheet(request):
    print("\n\n Scoresheet! \n\n")
    context = {}
    players = Tournament.objects.all().filter(date=date.today())

    for player in players:
        user = str(request.user)
        if (user == player.user_id):
            context = {
                'player' : player
            }

    return render(request, "PuttPutt/scoresheet.html", context)

# Saves the users scorecard for the current tournament
def saveScorecard(request):
    score_1 = request.POST['score_1']
    score_2 = request.POST['score_2']
    score_3 = request.POST['score_3']
    score_4 = request.POST['score_4']
    score_5 = request.POST['score_5']
    score_6 = request.POST['score_6']
    score_7 = request.POST['score_7']
    score_8 = request.POST['score_8']
    score_9 = request.POST['score_9']
    context = {}
    players = Tournament.objects.all().filter(date=date.today())

    for player in players:
        user = str(request.user)
        if (user == player.user_id):
            player.score_hole_1 = score_1
            player.score_hole_2 = score_2
            player.score_hole_3 = score_3
            player.score_hole_4 = score_4
            player.score_hole_5 = score_5
            player.score_hole_6 = score_6
            player.score_hole_7 = score_7
            player.score_hole_8 = score_8
            player.score_hole_9 = score_9
            player.save()

    return redirect('playerDashboard')

# Takes user to the sponsor dashboard
def sponsorDashboard(request):
    print("\n\n Sponsor Dashboard!\n\n")
    tournaments = Calendar.objects.all()
    context = {
        'tournaments' : tournaments
    }

    if (request.user.profile.user_type == "PL"):
        return redirect("playerDashboard")
    elif (request.user.profile.user_type == "SP"):
        return render(request, "PuttPutt/sponsorDashboard.html", context)
    elif (request.user.profile.user_type == "MA"):
        return redirect('managerDashboard')
    elif (request.user.profile.user_type == "DM"):
        return redirect('drinkmeisterDashboard')

# Takes input from sponsor user and sponsors a new tournament
def sponsorTournament(request):
    tournaments = Calendar.objects.all()
    context = {
        'tournaments' : tournaments
    }
    date = request.POST['datetimepicker']
    if (date != ""):
        date = date[0:10].replace("/", "-")
        prizeAmount = request.POST['prizeAmount']
        if prizeAmount != "":
            sponsor = request.user.username

            calenderTournament = Calendar()
            calenderTournament.date = date
            calenderTournament.prize_pool = prizeAmount
            calenderTournament.sponsor = sponsor
            calenderTournament.save()
        else:
            context = {
                'tournaments' : tournaments,
                'errors' : "Enter in a valid Prize Amount"
            }
    else:
        context = {
            'tournaments' : tournaments,
            'errors' : "Enter in a valid date"
        }

    return render(request, "PuttPutt/sponsorDashboard.html", context)

# Checks if user exists, and if their password is correct. If it is then they will go to the user dashboard
def signInUser(request):
    userName = request.POST['userID']
    password = request.POST['password']

    myUser = authenticate(username=userName, password=password)

    if (myUser is not None):
        auth.login(request=request, user=myUser)

        return playerDashboard(request)
    else:
        context = {
            'error' : "Username or Password is incorrect"
        }
        return render(request, "PuttPutt/loginPage.html", context)

# This just reloads the same page you're on, but executes the print function inside the terminal.
def testButtonFunction(request):
    print("\n\nDebugger button pressed! This is where you will execute code for database debugging.\n\n")

    return HttpResponse("""<html><script>window.location.replace('/databaseDebugger');</script></html>""")

# Updates the users type
def updateUserType(request):
    userChoice = request.POST['userChoice']
    userType = request.POST['userType']
    allUsers = User.objects.all()

    if (userChoice != ""):
        for user in allUsers:
            if (user.username == userChoice):
                user.profile.user_type = userType
                user.profile.save()
                return redirect('playerDashboard')
    else:
        context = {
            'users' : allUsers,
            'errors' : "Invalid User"
        }

        return render(request, "PuttPutt/manageUsers.html", context)

# Updates the drink menu
def updateDrink(request):
    drinkChoice = request.POST['drinkChoice']
    allDrinks = Drink.objects.all()

    if (drinkChoice != ""):
        for drink in allDrinks:
            if (str(drink) == drinkChoice):
                drink.delete()
                return redirect('manageDrinks')
    else:
        context = {
            'drinks' : allDrinks,
            'errors' : "Invalid Drink"
        }

        return render(request, "PuttPutt/manageDrinks.html", context)

def upcomingTournaments(request):
    tournaments = Calendar.objects.all()
    context = {
        'tournaments' : tournaments
    }

    return render(request, "PuttPutt/upcomingTournaments.html", context)
