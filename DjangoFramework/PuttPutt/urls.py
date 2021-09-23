from django.urls import path

from PuttPutt import views

urlpatterns = [
    path('', views.index, name="index"),
    path('databaseDebugger', views.databaseDebugger, name="debugger"),
    path('testButtonFunction', views.testButtonFunction),
]
