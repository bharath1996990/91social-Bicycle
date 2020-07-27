from django.urls import path
from .views import estimate_cycle_cost



urlpatterns = [
      path('estimate_cycle_cost/', estimate_cycle_cost, name='estimate_cycle_cost'),
]