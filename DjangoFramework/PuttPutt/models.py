from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=14)
    password = models.CharField(max_length=21)
    account_balance = models.FloatField(default=0)