from django.db import models


class Restaurants(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128, blank=True)


class Pizzas(models.Model):
    name = models.CharField(max_length=128)
    cheese = models.CharField(max_length=128, blank=True)
    pastry = models.CharField(max_length=128, blank=True)
    secret_ingredient = models.CharField(max_length=128, blank=True)
    restaurant = models.ManyToManyField(Restaurants)
