from PuttPutt.models import User
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


### Creates user from input from the create user page
def createUser(request):
    user_name = request.GET['userName']
    password = request.GET['password']
    user_id = request.GET['userID']

    user = User()
    user.user_name = user_name
    user.password = password
    user.user_id = user_id
    user.save()

    return HttpResponse("""<html><script>window.location.replace('/databaseDebugger');</script></html>""")
