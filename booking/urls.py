from django.urls import path
from .views import booking
app_name = 'booking'
urlpatterns = [
    path('booking/', booking, name="booking")
]
