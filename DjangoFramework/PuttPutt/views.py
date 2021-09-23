from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "PuttPutt/index.html")


def databaseDebugger(request):
    return render(request, "PuttPutt/databaseDebugger.html")


def testButtonFunction(request):
    print("\n\nDebugger button pressed! This is where you will execute code for database debugging.\n\n")

    ### This just reloads the same page you're on, but executes the print function inside the terminal.
    return HttpResponse("""<html><script>window.location.replace('/databaseDebugger');</script></html>""")