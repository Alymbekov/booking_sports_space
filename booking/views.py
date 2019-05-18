
from django.http import HttpResponse
from booking.models import Field, Image


def booking(request):
    fields = Field.objects.all()
    image = Image.objects.all()
    return render(request, 'booking/booking.html', {
        'fields': fields,
        'images': image,
    })





# Create your views here.
