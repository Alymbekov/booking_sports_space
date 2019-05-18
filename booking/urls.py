from django.urls import path
from .views import booking
from . import views

from booking.views import FieldCreateView


app_name = 'booking'
urlpatterns = [
    path('booking/', booking, name="booking"),
    path('add/', FieldCreateView.as_view(), name="create-field"),
    path('', views.FieldList.as_view(), name='field_list'),
    path('view/<int:pk>', views.FieldView.as_view(), name='field_view'),
    path('new', views.FieldCreate.as_view(), name='field_new'),
    path('view/<int:pk>', views.FieldView.as_view(), name='field_view'),
    path('edit/<int:pk>', views.FieldUpdate.as_view(), name='field_edit'),
    path('delete/<int:pk>', views.FieldDelete.as_view(), name='field_delete')
]

