from django import path
from .import views

urlpatterns = [
    path('travel-booking-form/', views.travelform, name='travel')
]