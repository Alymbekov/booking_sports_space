from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UsernameField
from django.forms import widgets


class UserCreationForm(forms.ModelForm):
    username = UsernameField(
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}),
    )
    email = forms.EmailField(
        required=True,
        widget=widgets.EmailInput(attrs={
            'class': 'form-control'
        }),
    )

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password',)
        widgets = {
            'password': widgets.PasswordInput(attrs={'class': 'form-control'}),
        }

    def clean_email(self):
        email = self.cleaned_data["email"]
        users_found = get_user_model().objects.filter(email__iexact=email).exists()

        if users_found:
            raise forms.ValidationError("A user with that email already exist.")

        return email

    def save(self):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.email = self.cleaned_data["email"]
        user.is_active = False
        user.save()
        return user