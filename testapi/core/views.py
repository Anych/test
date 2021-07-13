from rest_framework import viewsets

from core.models import Restaurants, Pizzas
from core.serializers import RestaurantsSerializer, PizzasSerializer


class RestaurantsViewSet(viewsets.ModelViewSet):
    """Manage restaurants in the database"""
    serializer_class = RestaurantsSerializer
    queryset = Restaurants.objects.all()


class PizzasViewSet(viewsets.ModelViewSet):
    """Manage pizzas in the database"""
    serializer_class = PizzasSerializer
    queryset = Pizzas.objects.all()
