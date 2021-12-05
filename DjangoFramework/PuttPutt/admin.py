from django.contrib import admin
from PuttPutt.models import Drink
from PuttPutt.models import DrinkOrders
from PuttPutt.models import Profile
from PuttPutt.models import Calendar
from PuttPutt.models import Tournament

# Register your models here.
admin.site.register(Drink)
admin.site.register(DrinkOrders)
admin.site.register(Profile)
admin.site.register(Calendar)
admin.site.register(Tournament)
