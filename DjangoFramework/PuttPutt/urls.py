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
    path('playerDashboard', views.playerDashboard),
]
