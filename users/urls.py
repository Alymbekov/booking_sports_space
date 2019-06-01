from django.urls import path
from .views import RegistrationView, ActivationView

app_name = 'users'

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('activate/<str:uidb64>/<str:token>/', ActivationView.as_view(), name='activation'),


]
