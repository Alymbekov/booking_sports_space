from django.urls import path
from .views import *

app_name = 'booking'
urlpatterns = [
    path('', index, name= "index"),
    path('booking/', booking, name="booking"),
    path('add/', FieldCreateView.as_view(), name="create-field"),
    path('field-list/', FieldList.as_view(), name='field_list'),
    path('view/<int:pk>/', FieldView.as_view(), name='field_view'),
    path('edit/<int:pk>/', FieldUpdate.as_view(), name='field_edit'),
    path('delete/<int:pk>/', FieldDelete.as_view(), name='field_delete')
]
