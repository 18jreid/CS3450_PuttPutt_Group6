from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date
from django import utils

# Create your models here.

# keeps track of additional info for our users
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    PLAYER = 'PL'
    SPONSOR = 'SP'
    MANAGER = 'MA'
    DRINKMEISTER = 'DM'

    USER_TYPE_CHOICES = [
        (PLAYER, 'Player'),
        (SPONSOR, 'Sponsor'),
        (MANAGER, 'Manager'),
        (DRINKMEISTER, 'DrinkMeister'),
    ]

    user_type = models.CharField(
        max_length = 2,
        choices = USER_TYPE_CHOICES,
        default = PLAYER
    )

    account_balance = models.FloatField(default=0)

# create a profile when user accounts are created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created: 
        Profile.objects.create(user=instance)

# when user accounts are updated, also update their profile
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Tournament(models.Model):
    date = models.DateField(default= utils.timezone.now)
    user_id = models.CharField(max_length=14)
    score_hole_1 = models.PositiveSmallIntegerField(default=0)
    score_hole_2 = models.PositiveSmallIntegerField(default=0)
    score_hole_3 = models.PositiveSmallIntegerField(default=0)
    score_hole_4 = models.PositiveSmallIntegerField(default=0)
    score_hole_5 = models.PositiveSmallIntegerField(default=0)
    score_hole_6 = models.PositiveSmallIntegerField(default=0)
    score_hole_7 = models.PositiveSmallIntegerField(default=0)
    score_hole_8 = models.PositiveSmallIntegerField(default=0)
    score_hole_9 = models.PositiveSmallIntegerField(default=0)
    score_hole_10 = models.PositiveSmallIntegerField(default=0)
    score_hole_11 = models.PositiveSmallIntegerField(default=0)
    score_hole_12 = models.PositiveSmallIntegerField(default=0)
    score_hole_13 = models.PositiveSmallIntegerField(default=0)
    score_hole_14 = models.PositiveSmallIntegerField(default=0)
    score_hole_15 = models.PositiveSmallIntegerField(default=0)
    score_hole_16 = models.PositiveSmallIntegerField(default=0)
    score_hole_17 = models.PositiveSmallIntegerField(default=0)
    score_hole_18 = models.PositiveSmallIntegerField(default=0)

    @property
    def scoreSum(self):
        total = self.score_hole_1 + self.score_hole_2 + self.score_hole_3 + self.score_hole_4 + self.score_hole_5 + self.score_hole_6 + self.score_hole_7 + self.score_hole_8 + self.score_hole_9 + self.score_hole_10 + self.score_hole_11 + self.score_hole_12 + self.score_hole_13 + self.score_hole_14 + self.score_hole_15 + self.score_hole_16 + self.score_hole_17 + self.score_hole_18

        return total

    @property
    def getUserName(self):
        allUsers = User.objects.all()
        name = "No Name"
        for user in allUsers:
            if (self.user_id == user.username):
                name = user.get_full_name()
        
        return name


class Calendar(models.Model):
    date = models.DateField()
    tournament_scheduled = models.BooleanField(default = False)
    prize_pool = models.PositiveIntegerField()
    sponsor = models.CharField(max_length=50)


class Drink(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    cost = models.FloatField(default=0)


class DrinkOrder(models.Model):
    user_id = models.CharField(max_length=14)
    drink = models.CharField(max_length=30)
    hole_number = models.PositiveSmallIntegerField(default=0)
    time_created = models.DateTimeField(auto_now_add=True)


