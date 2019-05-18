from django.shortcuts import render
from django.http import HttpResponse
from booking.models import Field


def booking(request):
    fields = Field.objects.all()
    return render(request, 'booking/booking.html', {
        'fields': fields,
    })




    
# Create your views here.
