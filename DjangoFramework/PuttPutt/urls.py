from django.conf.urls import url
from django.urls import path
from PuttPutt import views

urlpatterns = [
    path('', views.index, name="index"),
    path('addFunds', views.addFunds, name="addFunds"),
    path('addMoney', views.addMoney, name="addMoney"),
    path('createDrinkPage', views.createDrinkPage),
    path('createDrink', views.createDrink),
    path('createUserPage', views.createUserPage),
    path('createUser', views.createUser),
    path('currentTournament', views.currentTournament, name="currentTournament"),
    path('databaseDebugger', views.databaseDebugger, name="debugger"),
    path('drinkDemo', views.drinkDemo, name="drinkDemo"),
    path('drinkmeisterDashboard', views.drinkmeisterDashboard, name="drinkmeisterDashboard"),
    path('joinTournament', views.joinTournament, name="joinTournament"),
    path('loginPage', views.login, name="login"),
    path('logout', views.logout_user, name='logout'),
    path('managerDashboard', views.managerDashboard, name="managerDashboard"),
    path('manageCurrentTournament', views.manageCurrentTournament, name="manageCurrentTournament"),
    path('manageUsers', views.manageUsers, name="manageUsers"),
    path('orderDrinks', views.orderDrinks, name="orderDrinks"),
    path('playerDashboard', views.playerDashboard, name="playerDashboard"),
    path('sponsorDashboard', views.sponsorDashboard, name="sponsorDashboard"),
    path('sponsorTournament', views.sponsorTournament, name="sponsorTournament"),
    path('saveScorecard', views.saveScorecard, name="saveScorecard"),
    path('scoresheet', views.scoresheet, name="scoresheet"),
    path('signInUser', views.signInUser),
    path('upcomingTournaments', views.upcomingTournaments, name="upcomingTournaments"),
    path('testButtonFunction', views.testButtonFunction),
    path('updateUserType', views.updateUserType, name="updateUserType")
]
