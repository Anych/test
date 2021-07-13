from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views import PizzasViewSet, RestaurantsViewSet

router = DefaultRouter()
router.register('pizzas', PizzasViewSet)
router.register('restaurants', RestaurantsViewSet)

app_name = 'core'

urlpatterns = [
    path('', include(router.urls)),
]
