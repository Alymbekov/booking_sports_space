from django import forms
from django.forms import widgets
from booking.models import Field

class FieldForm(forms.ModelForm):



    class Meta:
        model = Field
        fields = ('title','description','address', 'image')
        widgets = {
            'title': widgets.TextInput(attrs={'class': 'form-control'}),
        }