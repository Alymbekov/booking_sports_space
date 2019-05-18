from django.urls import path
from .views import booking, IndexView

app_name = 'website'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('booking/', booking, name="booking"),
]
