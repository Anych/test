from django.db import models

from restaurants.models import Restaurants


class Pizzas(models.Model):
    name = models.CharField(max_length=128)
    cheese = models.CharField(max_length=128)
    pastry = models.CharField(max_length=128)
    secret_ingredient = models.CharField(max_length=128)
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
