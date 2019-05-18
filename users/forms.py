from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


choices = (
    ('spaceadmin', 'SportSpaceAdmin'),
    ('customer', 'Customer'),
)


class UserForm(UserCreationForm):
    type_of_user = forms.CharField(
        label="Тип пользователя",
        widget=forms.RadioSelect(
            choices=choices
        )
    )

    class Meta:
        model=User
        fields = ['full_name', 'email', 'password1', 'password2', 'type_of_user']
