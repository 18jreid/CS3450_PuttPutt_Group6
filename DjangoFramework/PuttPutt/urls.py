from django.urls import path

from PuttPutt import views

urlpatterns = [
    path('', views.index, name="index"),
]
