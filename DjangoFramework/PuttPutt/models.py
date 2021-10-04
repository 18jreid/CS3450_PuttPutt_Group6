from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=14)

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

    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=21)
    account_balance = models.FloatField(default=0)

class Tournament(models.Model):
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

class Calendar(models.Model):
    date = models.DateField()
    tournament_scheduled = models.BooleanField(default = False)
    prize_pool = models.PositiveIntegerField()
    sponsor = models.CharField(max_length=50)

class Drinks(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    cost = models.FloatField(default=0)

class DrinkOrders(models.Model):
    user_id = models.CharField(max_length=12)
    drink = models.CharField(max_length=30)
    hole_number = models.PositiveSmallIntegerField(default=0)


