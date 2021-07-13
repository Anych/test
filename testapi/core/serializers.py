from rest_framework import serializers

from core.models import Restaurants, Pizzas


class PizzasSerializer(serializers.ModelSerializer):
    """Serializer for pizzas objects"""

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    restaurant = serializers.PrimaryKeyRelatedField(
        many=True,
        required=True,
        queryset=Restaurants.objects.all(),
    )

    class Meta:
        model = Pizzas
        fields = ('id', 'name', 'cheese', 'pastry', 'secret_ingredient', 'restaurant')
        read_only_fields = ('id',)


class RestaurantsSerializer(serializers.ModelSerializer):
    """Serializer for restaurants objects"""

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    class Meta:
        model = Restaurants
        fields = ('id', 'name', 'address')
        read_only_fields = ('id',)