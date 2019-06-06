from django import forms
from django.forms import widgets
from booking.models import Field

class FieldForm(forms.ModelForm):



    class Meta:
        model = Field
        fields = ('title','description','address', 'image', 'open_time', 'close_time', 'parking')
        widgets = {
            'title': widgets.TextInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),

            'description': widgets.Textarea(attrs={'class': 'form-control','rows': 4}),
        }