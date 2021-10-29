from django.conf.urls import url
from django.urls import path
from PuttPutt import views

urlpatterns = [
    path('', views.index, name="index"),
    path('databaseDebugger', views.databaseDebugger, name="debugger"),
    path('drinkDemo', views.drinkDemo, name="drinkDemo"),
    path('testButtonFunction', views.testButtonFunction),
    path('createDrinkPage', views.createDrinkPage),
    path('createDrink', views.createDrink),
    path('createUserPage', views.createUserPage),
    path('createUser', views.createUser),
    path('playerDashboard', views.playerDashboard, name="playerDashboard"),
    path('drinkmeisterDashboard', views.drinkmeisterDashboard, name="drinkmeisterDashboard"),
    path('sponsorDashboard', views.sponsorDashboard, name="sponsorDashboard"),
    path('managerDashboard', views.managerDashboard, name="managerDashboard"),
    path('manageUsers', views.manageUsers, name="manageUsers"),
    path('loginPage', views.login, name="login"),
    path('signInUser', views.signInUser),
    path('logout', views.logout_user, name='logout')
]
