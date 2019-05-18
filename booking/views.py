from django.shortcuts import render
from django.http import HttpResponse
from booking.models import Field, Image
from django.views.generic import TemplateView

def booking(request):
    fields = Field.objects.all()
    image = Image.objects.all()
    return render(request, 'booking/booking.html', {
        'fields': fields,
        'images': image,
    })

class IndexView(TemplateView):
    template_name = 'website/main.html'




# Create your views here.
