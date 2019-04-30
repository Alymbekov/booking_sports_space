from django.urls import path
from booking.views import index

urlpatterns = [
    path('index/', index, name="index")
]
