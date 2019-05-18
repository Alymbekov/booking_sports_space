from django import forms
from booking.models import Field

class FieldForm(forms.ModelForm):



    class Meta:
        model = Field
        fields = ('title','description','address')