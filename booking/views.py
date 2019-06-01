from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from booking.forms import FieldForm

from booking.models import Field, Image
from django.urls import reverse_lazy


def booking(request):
    fields = Field.objects.all()
    image = Image.objects.all()
    return render(request, 'booking/booking.html', {
        'fields': fields,
        'images': image,
    })

@method_decorator(login_required, name='dispatch')
class FieldCreateView(CreateView):
    template_name = 'booking/create-field.html'
    model = Field
    form_class = FieldForm
    success_url = reverse_lazy('booking:field_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class FieldList(ListView):
    model = Field


class FieldView(DetailView):
    model = Field


class FieldUpdate(UpdateView):
    model = Field
    fields = ['title', 'pages']
    success_url = reverse_lazy('field_list')


class FieldDelete(DeleteView):
    model = Field
    fields = ['title', 'pages']
    success_url = reverse_lazy('field_list')

# Create your views here.
